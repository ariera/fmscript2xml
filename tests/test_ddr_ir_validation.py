"""Validation tests against DDR IR reference XML."""

import xml.etree.ElementTree as ET

import pytest

from fmscript2xml import Converter
from tests.utils.ddr_ir_loader import find_step_by_name
from tests.utils.fixture_utils import generate_reference_from_ddr_ir


def pytest_generate_tests(metafunc):
    if "step_id" in metafunc.fixturenames:
        step_ids = sorted(metafunc.config._ddr_ir.keys())
        metafunc.parametrize("step_id", step_ids)


def test_step_against_ddr_ir(step_id, ddr_ir):
    # Intentionally skip steps with known DDR IR XML issues that need manual fixing
    # These steps have malformed XML in the DDR IR that cannot be automatically fixed
    intentionally_skipped_steps = {91, 134, 135, 136, 137, 138, 143, 144, 161}
    if step_id in intentionally_skipped_steps:
        pytest.skip(f"Step {step_id} intentionally skipped due to DDR IR XML malformation issues")

    step_info = ddr_ir.get(step_id)
    if not step_info:
        pytest.skip(f"No DDR IR info for step {step_id}")

    # Get step name from YAML, but prefer the actual name from XML if YAML name is invalid
    step_name_yaml = step_info.get("name")
    if not step_name_yaml:
        pytest.skip(f"No step name for step {step_id}")

    # Get reference XML first to extract actual step name
    reference_xml = generate_reference_from_ddr_ir(step_id)
    if not reference_xml:
        pytest.skip(f"No reference XML for step {step_id}")

    expected_step = _first_step(reference_xml)
    if expected_step is None:
        pytest.fail(f"Reference XML for step {step_id} contains invalid XML (likely placeholders)")

    # Get the actual step name from the XML (might differ from YAML due to parsing issues)
    actual_step_name = expected_step.attrib.get("name")
    if not actual_step_name:
        pytest.fail(f"No step name in reference XML for step {step_id}")

    # For steps with HTML-like names in YAML (parsing errors), use XML name
    if step_name_yaml.startswith("<"):
        step_name_to_use = actual_step_name
    else:
        step_name_to_use = step_name_yaml

    # Parser strips trailing spaces, so use the stripped version for conversion
    step_name_for_conversion = step_name_to_use.rstrip()

    # Verify step is registered (registry.get now handles trailing spaces)
    converter = Converter()
    step_def = converter.registry.get(step_name_for_conversion)

    if step_def is None:
        pytest.fail(f"Step '{step_name_for_conversion}' is not registered in step registry. "
                   f"Please add step definition file for step ID {step_id} (YAML name: '{step_name_yaml}').")

    # Minimal input: use the step name that will work with the parser
    generated_xml = converter.convert(step_name_for_conversion, stop_on_error=False)

    # Skip helper comment steps when finding the generated step
    generated_step = _first_step(generated_xml, skip_comments=True)
    if generated_step is None:
        pytest.fail(f"No Step found in generated XML for '{step_name_for_conversion}'. "
                   f"Generated XML: {generated_xml[:500]}")

    # Compare core attributes only for minimal inputs
    assert expected_step.attrib.get("name") == generated_step.attrib.get("name"), \
        f"Step name mismatch: expected '{expected_step.attrib.get('name')}', got '{generated_step.attrib.get('name')}'"
    assert expected_step.attrib.get("id") == generated_step.attrib.get("id"), \
        f"Step ID mismatch: expected '{expected_step.attrib.get('id')}', got '{generated_step.attrib.get('id')}'"


def _first_step(xml_string: str, skip_comments: bool = False):
    """Extract first Step element from XML, optionally skipping Comment steps."""
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        # XML might contain placeholders like {name} - skip this test
        return None

    for child in list(root):
        if child.tag == "Step":
            # Skip helper comment steps if requested
            if skip_comments and child.attrib.get("name") == "Comment":
                text_elem = child.find("Text")
                if text_elem is not None and (text_elem.text or "").strip().startswith("Original:"):
                    continue
            return child
    return None
