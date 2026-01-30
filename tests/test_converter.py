"""Integration tests for converter."""

import pytest
from pathlib import Path
from fmscript2xml import Converter, UnknownStepError


class TestConverter:
    """Test converter functionality."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_convert_simple_script(self, converter):
        """Test converting a simple script."""
        text = """# Comment
Set Variable [ $var ; Value: 1 ]"""

        xml = converter.convert(text)

        assert "<fmxmlsnippet" in xml
        assert "Set Variable" in xml
        assert "$var" in xml or "var" in xml

    def test_convert_comment(self, converter):
        """Test converting a comment."""
        text = "# This is a comment"

        xml = converter.convert(text)

        assert "<fmxmlsnippet" in xml
        assert "Comment" in xml
        assert "This is a comment" in xml

    def test_convert_if_statement(self, converter):
        """Test converting If statement."""
        text = """If [ Get ( FoundCount ) = 0 ]
    Exit Script
End If"""

        xml = converter.convert(text)

        assert "<fmxmlsnippet" in xml
        assert "If" in xml
        assert "End If" in xml

    def test_unknown_step_error(self, converter):
        """Test that unknown steps raise error."""
        text = "Unknown Step [ param: value ]"

        with pytest.raises(UnknownStepError):
            converter.convert(text)

    def test_unknown_step_continue(self, converter):
        """Test that unknown steps can be skipped."""
        text = "Unknown Step [ param: value ]"

        xml = converter.convert(text, stop_on_error=False)

        # Should still produce XML (with error comment)
        assert "<fmxmlsnippet" in xml

    def test_validate(self, converter):
        """Test validation."""
        # Valid script
        text = "Set Variable [ $var ; Value: 1 ]"
        is_valid, errors = converter.validate(text)
        assert is_valid
        assert len(errors) == 0

        # Invalid script (unknown step)
        text = "Unknown Step [ param: value ]"
        is_valid, errors = converter.validate(text)
        assert not is_valid
        assert len(errors) > 0

    def test_complex_real_world_script(self, converter):
        """Test a complex real-world script scenario."""
        text = """# Init result vars
Set Variable [ $ForceShowMessage ; Value: 0 ]
Set Variable [ $ResultTitle ; Value: "" ]
Set Variable [ $scriptParameter ; Value: Get ( ScriptParameter ) ]
If [ IsEmpty ( $scriptParameter ) ]
  Set Variable [ $ResultTitle ; Value: "Create/Update forms failed" ]
  Exit Script [ Text Result: $finalScriptResult ]
End If
Set Variable [ $groupId ; Value: JSONGetElement ( $ResultMessage ; "group_id" ) ]
Go to Layout [ $returnLayout ]"""

        xml = converter.convert(text)

        # Verify all key components
        assert "$ForceShowMessage" in xml
        assert '""' in xml
        assert "Get ( ScriptParameter )" in xml
        assert "IsEmpty ( $scriptParameter )" in xml
        assert '"Create/Update forms failed"' in xml
        assert "$finalScriptResult" in xml
        assert "JSONGetElement ( $ResultMessage ; \"group_id\" )" in xml
        assert "LayoutNameByCalc" in xml
        assert "$returnLayout" in xml

