"""Real-world script fixture tests."""

from pathlib import Path

import pytest

from fmscript2xml import Converter
from tests.utils.fixture_utils import list_fixtures, validate_fixture
from tests.utils.semantic_comparator import compare_xml, format_diff


def pytest_generate_tests(metafunc):
    if "fixture_path" in metafunc.fixturenames:
        fixtures = list_fixtures()
        metafunc.parametrize("fixture_path", fixtures, ids=[p.name for p in fixtures])


def test_real_world_script(fixture_path: Path, ddr_ir):
    if not validate_fixture(fixture_path):
        pytest.skip(f"Invalid fixture: {fixture_path}")

    input_text = (fixture_path / "input.txt").read_text(encoding="utf-8")
    expected_xml = (fixture_path / "expected.xml").read_text(encoding="utf-8")

    converter = Converter()
    generated_xml = converter.convert(input_text, stop_on_error=False)

    result = compare_xml(expected_xml, generated_xml, ddr_ir=ddr_ir)
    if not result.is_equal:
        pytest.fail(format_diff(result))
