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
    step_info = ddr_ir.get(step_id)
    if not step_info:
        pytest.skip(f"No DDR IR info for step {step_id}")

    step_name = step_info.get("name")
    if not step_name:
        pytest.skip(f"No step name for step {step_id}")

    converter = Converter()
    registry_id = find_step_by_name(step_name)
    if registry_id is None:
        pytest.skip(f"Step not registered: {step_name}")

    # Minimal input: step name only
    generated_xml = converter.convert(step_name, stop_on_error=False)

    # Reference XML (wrapped)
    reference_xml = generate_reference_from_ddr_ir(step_id)
    if not reference_xml:
        pytest.skip(f"No reference XML for step {step_id}")

    expected_step = _first_step(reference_xml)
    generated_step = _first_step(generated_xml)

    assert expected_step is not None, f"No Step in reference XML for {step_name}"
    assert generated_step is not None, f"No Step in generated XML for {step_name}"

    # Compare core attributes only for minimal inputs
    assert expected_step.attrib.get("name") == generated_step.attrib.get("name")
    assert expected_step.attrib.get("id") == generated_step.attrib.get("id")


def _first_step(xml_string: str):
    root = ET.fromstring(xml_string)
    for child in list(root):
        if child.tag == "Step":
            return child
    return None
