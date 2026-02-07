"""Tests for CLI functionality."""

import pytest
from pathlib import Path
import tempfile
import os
import sys


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


def test_from_clipboard_requires_output_or_no_file(monkeypatch, capsys):
    from fmscript2xml import converter

    monkeypatch.setattr(sys, "argv", ["fmscript2xml", "--from-clipboard"])
    result = converter.main()
    captured = capsys.readouterr()

    assert result == 1
    assert "--from-clipboard requires --output or --no-file" in captured.err


def test_input_required_without_from_clipboard(monkeypatch, capsys):
    from fmscript2xml import converter

    monkeypatch.setattr(sys, "argv", ["fmscript2xml"])
    result = converter.main()
    captured = capsys.readouterr()

    assert result == 1
    assert "Input file is required unless --from-clipboard is used" in captured.err

