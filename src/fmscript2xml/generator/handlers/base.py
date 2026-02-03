"""
Base handler class for step handlers.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep


class StepHandler:
    """Base class for step handlers."""

    def can_handle(self, step: ParsedStep, step_def: dict) -> bool:
        """Check if this handler can handle the given step."""
        return step.name == step_def['name']

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        """
        Generate XML elements for this step.

        Args:
            step: Parsed step data
            step_def: Step definition dict with keys: id, name, xml_step_name, enable_default

        Returns:
            List of Step elements (may include helper comments)
        """
        raise NotImplementedError
