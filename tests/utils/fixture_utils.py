"""Fixture utilities for real-world script tests."""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from .ddr_ir_loader import load_ddr_ir, get_step_reference_xml


def create_fixture(script_name: str, input_text: str, expected_xml: str) -> Path:
    """Create a fixture folder with input.txt and expected.xml."""
    base_dir = Path(__file__).resolve().parents[2] / "fixtures" / "real_world"
    fixture_dir = base_dir / script_name
    fixture_dir.mkdir(parents=True, exist_ok=True)

    (fixture_dir / "input.txt").write_text(input_text, encoding="utf-8")
    (fixture_dir / "expected.xml").write_text(expected_xml, encoding="utf-8")

    return fixture_dir


def validate_fixture(fixture_path: Path) -> bool:
    """Validate that a fixture has required files."""
    fixture_path = Path(fixture_path)
    return (fixture_path / "input.txt").exists() and (fixture_path / "expected.xml").exists()


def list_fixtures() -> List[Path]:
    """List all fixture directories under tests/fixtures/real_world."""
    base_dir = Path(__file__).resolve().parents[2] / "fixtures" / "real_world"
    if not base_dir.exists():
        return []
    return [p for p in base_dir.iterdir() if p.is_dir()]


def generate_reference_from_ddr_ir(step_id: int) -> Optional[str]:
    """Generate fmxmlsnippet XML from DDR IR reference for a step."""
    steps_dir = Path(__file__).resolve().parents[3] / "docs" / "DRR XML Grammar" / "ddr-ir" / "steps"
    load_ddr_ir(steps_dir)
    step_xml = get_step_reference_xml(step_id)
    if not step_xml:
        return None
    return _wrap_in_fmxmlsnippet(step_xml)


def _wrap_in_fmxmlsnippet(step_xml: str) -> str:
    return f'<?xml version="1.0" ?>\n<fmxmlsnippet type="FMObjectList">\n  {step_xml}\n</fmxmlsnippet>\n'
