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


    def test_multiline_string_keeps_line_breaks(self):
        """Line breaks and indentation inside a string literal are part of its value."""
        parser = Parser()
        text = 'Set Variable [ $sql ; Value: "SELECT a\n    FROM b" ]\nBeep'
        steps = parser.parse(text)

        assert [s.name for s in steps] == ["Set Variable", "Beep"]
        assert steps[0].params["Value"] == '"SELECT a\n    FROM b"'

    def test_multiline_calc_keeps_line_breaks_after_line_comment(self):
        """A // comment ends at the line break, so continuation lines must not be joined onto it."""
        parser = Parser()
        text = 'Set Variable [ $x ; Value: 1 & // first [ part\n    2 ]\nBeep'
        steps = parser.parse(text)

        assert [s.name for s in steps] == ["Set Variable", "Beep"]
        assert steps[0].params["Value"] == "1 & // first [ part\n    2"

    def test_comments_hide_brackets_and_separators(self):
        """Brackets, semicolons and colons inside calculation comments are not syntax."""
        parser = Parser()
        text = (
            'Set Variable [ $a ; Value: 1 /* see [ ; x: y */ ]\n'
            'Set Variable [ $b ; Value: 2 // note: b [c] ]\n'
            'Beep'
        )
        steps = parser.parse(text)

        assert [s.name for s in steps] == ["Set Variable", "Set Variable", "Beep"]
        assert steps[0].params == {"0": "$a", "Value": "1 /* see [ ; x: y */"}
        assert steps[1].params == {"0": "$b", "Value": "2 // note: b [c]"}

    def test_trailing_line_comment_before_step_close(self):
        """FileMaker appends the step's closing ] after a trailing // comment."""
        parser = Parser()
        text = 'If [ Get ( WindowMode ) = 1  // in FIND mode ]\nEnd If'
        steps = parser.parse(text)

        assert [s.name for s in steps] == ["If", "End If"]
        assert steps[0].params == {"0": "Get ( WindowMode ) = 1  // in FIND mode"}

    def test_trailing_line_comment_before_next_param(self):
        """FileMaker writes the next parameter after a trailing // comment on the same line."""
        parser = Parser()
        text = 'Set Field By Name [ Specify target field: ON ; $f // the target ; $id ]'
        steps = parser.parse(text)

        assert steps[0].params == {
            "Specify target field": "ON",
            "0": "$f // the target",
            "1": "$id",
        }
