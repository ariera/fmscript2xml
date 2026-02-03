"""
Loader for step definitions from pre-compiled JSON registry.

Loads minimal step metadata from the bundled steps.json file.
"""

import json
from pathlib import Path
from typing import Dict, Optional, List


class StepRegistry:
    """Registry of FileMaker script step definitions."""

    def __init__(self):
        """
        Initialize registry.

        Loads step definitions from the bundled steps.json file.
        """
        # Load from bundled JSON file
        registry_file = Path(__file__).parent.parent / "data" / "steps.json"

        if not registry_file.exists():
            raise FileNotFoundError(
                f"Steps registry not found: {registry_file}. "
                "Please run 'python scripts/build_steps_registry.py' to generate it."
            )

        with open(registry_file, 'r', encoding='utf-8') as f:
            self._definitions: Dict[str, dict] = json.load(f)

        self._loaded = True

    def get(self, step_name: str) -> Optional[dict]:
        """
        Get step definition by name.

        Args:
            step_name: Name of the step

        Returns:
            Dict with step metadata (id, name, xml_step_name, enable_default)
            or None if step not found
        """
        # Try exact match first
        step_def = self._definitions.get(step_name)
        if step_def:
            return step_def

        # Try with trailing space (parser strips trailing spaces, but registry might have them)
        if not step_name.endswith(' '):
            step_def = self._definitions.get(step_name + ' ')
            if step_def:
                return step_def

        # Try without trailing space (registry has space, but parser strips it)
        step_name_stripped = step_name.rstrip()
        if step_name_stripped != step_name:
            step_def = self._definitions.get(step_name_stripped)
            if step_def:
                return step_def

        return None

    def get_by_id(self, step_id: int) -> Optional[dict]:
        """
        Get step definition by ID.

        Args:
            step_id: ID of the step

        Returns:
            Dict with step metadata or None if step not found
        """
        for step_def in self._definitions.values():
            if step_def['id'] == step_id:
                return step_def
        return None

    def all_steps(self) -> List[dict]:
        """
        Get all step definitions.

        Returns:
            List of all step definition dicts
        """
        return list(self._definitions.values())

    def step_names(self) -> List[str]:
        """
        Get all step names.

        Returns:
            List of all step names
        """
        return list(self._definitions.keys())
