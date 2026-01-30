"""Tests for edge cases and error handling."""

import pytest
from fmscript2xml import Converter, UnknownStepError
from pathlib import Path


class TestEdgeCases:
    """Test edge cases and error handling."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_empty_input(self, converter):
        """Test empty input."""
        xml = converter.convert("")
        assert "<fmxmlsnippet" in xml

    def test_whitespace_only(self, converter):
        """Test whitespace-only input."""
        xml = converter.convert("   \n\n   ")
        assert "<fmxmlsnippet" in xml

    def test_multiple_comments(self, converter):
        """Test multiple comment lines."""
        text = """# First comment
# Second comment
# Third comment"""
        xml = converter.convert(text)

        assert xml.count("Comment") >= 3

    def test_nested_brackets_in_calculation(self, converter):
        """Test calculations with nested brackets."""
        text = 'Set Variable [ $result ; Value: If ( Get ( FoundCount ) > 0 ; "Yes" ; "No" ) ]'
        xml = converter.convert(text)

        assert "Set Variable" in xml
        assert "If" in xml or "FoundCount" in xml

    def test_quoted_strings(self, converter):
        """Test quoted string parameters."""
        text = 'Perform Script [ "MyScript" ]'
        xml = converter.convert(text)

        assert "Perform Script" in xml
        assert "MyScript" in xml

    def test_variables_in_calculations(self, converter):
        """Test variables in calculations."""
        text = 'Set Variable [ $sum ; Value: $a + $b ]'
        xml = converter.convert(text)

        assert "Set Variable" in xml
        assert "$sum" in xml or "sum" in xml

    def test_special_characters(self, converter):
        """Test special characters in text."""
        text = '# Comment with "quotes" and <brackets>'
        xml = converter.convert(text)

        assert "Comment" in xml

    def test_continue_on_error(self, converter):
        """Test continuing on error."""
        text = """Set Variable [ $var ; Value: 1 ]
Unknown Step [ param: value ]
Exit Script"""

        xml = converter.convert(text, stop_on_error=False)

        assert "Set Variable" in xml
        assert "Exit Script" in xml
        assert "ERROR" in xml or "Unknown" in xml

    def test_validation_with_errors(self, converter):
        """Test validation with errors."""
        text = "Unknown Step [ param: value ]"
        is_valid, errors = converter.validate(text)

        assert not is_valid
        assert len(errors) > 0
        assert "Unknown" in errors[0]

