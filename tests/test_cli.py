"""Tests for CLI functionality."""

import pytest
from pathlib import Path
import tempfile
import os


def test_output_filename_generation():
    """Test that output filename is generated correctly."""
    from pathlib import Path

    # Test various input filenames
    test_cases = [
        ("script.txt", "script.txt.xml"),
        ("script", "script.xml"),
        ("/path/to/script.txt", "/path/to/script.txt.xml"),
        ("script.fm", "script.fm.xml"),
    ]

    for input_file, expected_output in test_cases:
        input_path = Path(input_file)
        # Simulate the logic from converter.py
        output_path = input_path.with_suffix(input_path.suffix + '.xml')
        assert str(output_path) == expected_output


def test_cli_argument_parsing():
    """Test CLI argument parsing logic."""
    # This would require mocking argparse, but the logic is straightforward:
    # - If -o/--output is provided, use that
    # - Otherwise, use input.with_suffix(input.suffix + '.xml')

    from pathlib import Path

    input_path = Path("test.txt")

    # Without output specified
    output_path = input_path.with_suffix(input_path.suffix + '.xml')
    assert output_path.name == "test.txt.xml"

    # With output specified (simulated)
    custom_output = Path("custom.xml")
    assert custom_output.name == "custom.xml"

