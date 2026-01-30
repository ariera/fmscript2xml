"""Pytest configuration and shared fixtures."""

from pathlib import Path

import pytest

from fmscript2xml import Converter
from tests.utils.ddr_ir_loader import load_ddr_ir


def pytest_configure(config):
    steps_dir = Path(__file__).resolve().parents[1] / "docs" / "DRR XML Grammar" / "ddr-ir" / "steps"
    ddr_ir = load_ddr_ir(steps_dir)
    config._ddr_ir = ddr_ir


@pytest.fixture(scope="session")
def ddr_ir():
    steps_dir = Path(__file__).resolve().parents[1] / "docs" / "DRR XML Grammar" / "ddr-ir" / "steps"
    return load_ddr_ir(steps_dir)


@pytest.fixture(scope="session")
def converter():
    return Converter()


@pytest.fixture(scope="session")
def test_fixtures_path():
    return Path(__file__).resolve().parent / "fixtures"
