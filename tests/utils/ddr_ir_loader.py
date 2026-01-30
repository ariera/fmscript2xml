"""DDR IR loader for FileMaker step reference XML."""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

import yaml

_DDR_CACHE: Optional[Dict[int, Dict]] = None
_DDR_NAME_INDEX: Optional[Dict[str, int]] = None


def _normalize_step_name(name: str) -> str:
    return " ".join(name.strip().split()).lower()


def load_ddr_ir(steps_dir: Path) -> Dict[int, Dict]:
    """
    Load DDR IR step YAML files into a dict keyed by step ID.

    Args:
        steps_dir: Path to docs/DRR XML Grammar/ddr-ir/steps
    """
    global _DDR_CACHE, _DDR_NAME_INDEX
    if _DDR_CACHE is not None:
        return _DDR_CACHE

    steps_dir = Path(steps_dir)
    if not steps_dir.exists():
        raise FileNotFoundError(f"DDR IR steps directory not found: {steps_dir}")

    steps: Dict[int, Dict] = {}
    name_index: Dict[str, int] = {}

    for step_path in sorted(steps_dir.glob("*.yaml")):
        with step_path.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not data or "id" not in data:
            continue

        step_id = int(data["id"])
        steps[step_id] = data

        step_name = data.get("name")
        if step_name:
            name_index[_normalize_step_name(step_name)] = step_id

    _DDR_CACHE = steps
    _DDR_NAME_INDEX = name_index
    return steps


def get_step_reference_xml(step_id: int) -> Optional[str]:
    """Return fmxmlsnippet_xml for the given step ID."""
    if _DDR_CACHE is None:
        raise RuntimeError("DDR IR not loaded. Call load_ddr_ir() first.")
    step = _DDR_CACHE.get(step_id)
    if not step:
        return None
    return step.get("fmxmlsnippet_xml")


def get_step_info(step_id: int) -> Optional[Dict]:
    """Return full step info dict for the given step ID."""
    if _DDR_CACHE is None:
        raise RuntimeError("DDR IR not loaded. Call load_ddr_ir() first.")
    return _DDR_CACHE.get(step_id)


def find_step_by_name(name: str) -> Optional[int]:
    """Find step ID by step name (case/whitespace-insensitive)."""
    if _DDR_NAME_INDEX is None:
        raise RuntimeError("DDR IR not loaded. Call load_ddr_ir() first.")
    return _DDR_NAME_INDEX.get(_normalize_step_name(name))
