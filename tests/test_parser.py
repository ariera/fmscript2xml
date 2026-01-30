"""Tests for parser module."""

import pytest
from fmscript2xml.parser.parser import Parser, ParsedStep


class TestParser:
    """Test parser functionality."""

    def test_parse_simple_step(self):
        """Test parsing a simple step without parameters."""
        parser = Parser()
        steps = parser.parse("Comment")

        assert len(steps) == 1
        assert steps[0].name == "Comment"
        assert steps[0].params == {}

    def test_parse_step_with_params(self):
        """Test parsing a step with parameters."""
        parser = Parser()
        steps = parser.parse('Set Variable [ $var ; Value: 1 ]')

        assert len(steps) == 1
        assert steps[0].name == "Set Variable"
        assert "$var" in steps[0].params.get("Name", "") or "0" in steps[0].params
        assert "1" in str(steps[0].params.get("Value", steps[0].params.get("1", "")))

    def test_parse_comment(self):
        """Test parsing a comment line."""
        parser = Parser()
        steps = parser.parse("# This is a comment")

        assert len(steps) == 1
        assert steps[0].is_comment
        assert steps[0].name == "Comment"
        assert "This is a comment" in steps[0].comment_text

    def test_parse_multiple_steps(self):
        """Test parsing multiple steps."""
        parser = Parser()
        text = """Set Variable [ $var ; Value: 1 ]
If [ $var > 0 ]
    Exit Script
End If"""
        steps = parser.parse(text)

        assert len(steps) == 4
        assert steps[0].name == "Set Variable"
        assert steps[1].name == "If"
        assert steps[2].name == "Exit Script"
        assert steps[3].name == "End If"

    def test_parse_nested_brackets(self):
        """Test parsing steps with nested brackets in calculations."""
        parser = Parser()
        text = 'Set Variable [ $result ; Value: Get ( ScriptParameter ) ]'
        steps = parser.parse(text)

        assert len(steps) == 1
        assert steps[0].name == "Set Variable"
        # Calculation should be preserved
        assert "Get" in str(steps[0].params.values()) or "ScriptParameter" in str(steps[0].params.values())

