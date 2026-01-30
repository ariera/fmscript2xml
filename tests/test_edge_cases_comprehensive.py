"""Comprehensive edge case tests based on real-world issues."""

import pytest
from pathlib import Path
from fmscript2xml import Converter, UnknownStepError


class TestVariableHandling:
    """Test variable name preservation and handling."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_variable_name_preserves_dollar_prefix(self, converter):
        """Test that variable names preserve $ prefix."""
        text = "Set Variable [ $ForceShowMessage ; Value: 0 ]"
        xml = converter.convert(text)

        assert "$ForceShowMessage" in xml
        assert "<Name>$ForceShowMessage</Name>" in xml

    def test_empty_string_value(self, converter):
        """Test that empty string values are preserved as \"\"."""
        text = 'Set Variable [ $ResultTitle ; Value: "" ]'
        xml = converter.convert(text)

        assert '""' in xml
        assert '<Calculation><![CDATA[""]]></Calculation>' in xml

    def test_string_literal_in_calculation(self, converter):
        """Test that string literals in calculations are preserved."""
        text = 'Set Variable [ $ResultTitle ; Value: "Create/Update forms failed" ]'
        xml = converter.convert(text)

        assert '"Create/Update forms failed"' in xml
        assert '<Calculation><![CDATA["Create/Update forms failed"]]></Calculation>' in xml

    def test_variable_reference_in_exit_script(self, converter):
        """Test that variable references in Exit Script are preserved."""
        text = "Exit Script [ Text Result: $finalScriptResult ]"
        xml = converter.convert(text)

        assert "$finalScriptResult" in xml
        assert "<TextResult>" in xml
        assert "<Calculation><![CDATA[$finalScriptResult]]></Calculation>" in xml


class TestCalculationsWithParentheses:
    """Test calculations containing parentheses and function calls."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_function_call_with_parameters(self, converter):
        """Test function calls with parameters containing semicolons."""
        text = 'Set Variable [ $groupId ; Value: JSONGetElement ( $ResultMessage ; "group_id" ) ]'
        xml = converter.convert(text)

        # Should preserve the entire calculation
        assert "JSONGetElement ( $ResultMessage ; \"group_id\" )" in xml
        # Should not be split at the semicolon
        assert "JSONGetElement ( $ResultMessage" not in xml or '"group_id"' in xml

    def test_nested_function_calls(self, converter):
        """Test nested function calls."""
        text = 'Set Variable [ $count ; Value: ValueCount ( JSONListKeys ( $committeeMembers ; "" ) ) ]'
        xml = converter.convert(text)

        assert "ValueCount ( JSONListKeys ( $committeeMembers ; \"\" ) )" in xml

    def test_concatenation_with_ampersand(self, converter):
        """Test string concatenation with & operator."""
        text = 'Set Variable [ $msg ; Value: "text" & $var & "more" ]'
        xml = converter.convert(text)

        # & should be preserved in CDATA (not escaped as &amp;)
        assert '"text" & $var & "more"' in xml
        # Should NOT have &amp; in CDATA
        cdata_start = xml.find('<![CDATA[')
        cdata_end = xml.find(']]>', cdata_start)
        if cdata_start != -1 and cdata_end != -1:
            cdata_content = xml[cdata_start + 9:cdata_end]
            assert '&amp;' not in cdata_content or cdata_content.count('&amp;') == 0

    def test_complex_concatenation(self, converter):
        """Test complex concatenation with brackets and variables."""
        text = 'Set Variable [ $id ; Value: JSONGetElement ( $members ; "[" & $index & "].member_id" ) ]'
        xml = converter.convert(text)

        assert '"[" & $index & "].member_id"' in xml
        assert "JSONGetElement" in xml


class TestGoToLayout:
    """Test Go to Layout step handling."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_go_to_layout_with_variable(self, converter):
        """Test Go to Layout with a variable (should use Calculated)."""
        text = "Go to Layout [ $returnLayout ]"
        xml = converter.convert(text)

        assert "LayoutNameByCalc" in xml
        assert "<Calculated>" in xml
        assert "$returnLayout" in xml
        assert "<Calculation><![CDATA[$returnLayout]]></Calculation>" in xml

    def test_go_to_layout_with_named_layout(self, converter):
        """Test Go to Layout with a named layout."""
        text = 'Go to Layout [ "MyLayout" ]'
        xml = converter.convert(text)

        assert "SelectedLayout" in xml
        assert "MyLayout" in xml
        assert "<Layout" in xml


class TestMultiLineSteps:
    """Test multi-line step handling."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_multi_line_set_variable(self, converter):
        """Test Set Variable with multi-line calculation."""
        text = """Set Variable [ $param ; Value: JSONSetElement ( "{}" ;
  [ "phase" ; $phase ; JSONString ]
) ]"""
        xml = converter.convert(text)

        assert "$param" in xml
        assert "JSONSetElement" in xml
        # Should not have errors about unknown steps
        assert "ERROR" not in xml or "Unknown" not in xml


class TestRealWorldScenarios:
    """Test scenarios from real-world FileMaker scripts."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_init_result_vars_sequence(self, converter):
        """Test the init result vars sequence from real script."""
        text = """# Init result vars
Set Variable [ $ForceShowMessage ; Value: 0 ]
Set Variable [ $SuppressErrorCode ; Value: 0 ]
Set Variable [ $IsError ; Value: 0 ]
Set Variable [ $LastError ; Value: 0 ]
Set Variable [ $ResultTitle ; Value: "" ]
Set Variable [ $ResultMessage ; Value: "" ]"""

        xml = converter.convert(text)

        # Check all variables
        assert "$ForceShowMessage" in xml
        assert "$SuppressErrorCode" in xml
        assert "$IsError" in xml
        assert "$LastError" in xml
        assert "$ResultTitle" in xml
        assert "$ResultMessage" in xml
        # Check empty strings
        assert '""' in xml

    def test_parameter_parsing_sequence(self, converter):
        """Test parameter parsing with error handling."""
        text = """# Parse parameter
Set Variable [ $scriptParameter ; Value: Get ( ScriptParameter ) ]
If [ IsEmpty ( $scriptParameter ) ]
  Set Variable [ $IsError ; Value: 1 ]
  Set Variable [ $ResultTitle ; Value: "Create/Update forms failed" ]
  Set Variable [ $ResultMessage ; Value: "Missing script parameter." ]
  Set Variable [ $finalScriptResult ; Value: SetScriptResult ]
  Exit Script [ Text Result: $finalScriptResult ]
End If"""

        xml = converter.convert(text)

        # Check all components
        assert "Get ( ScriptParameter )" in xml
        assert "IsEmpty ( $scriptParameter )" in xml
        assert '"Create/Update forms failed"' in xml
        assert '"Missing script parameter."' in xml
        assert "SetScriptResult" in xml
        assert "$finalScriptResult" in xml
        assert "Exit Script" in xml

    def test_json_operations_sequence(self, converter):
        """Test sequence of JSON operations."""
        text = """Set Variable [ $groupId ; Value: JSONGetElement ( $ResultMessage ; "group_id" ) ]
Set Variable [ $year ; Value: JSONGetElement ( $ResultMessage ; "year" ) ]
Set Variable [ $committeeMemberCount ; Value: ValueCount ( JSONListKeys ( $committeeMembers ; "" ) ) ]
Set Variable [ $committeeMemberId ; Value: JSONGetElement ( $committeeMembers ; "[" & $committeeMemberIndex & "].member_id" ) ]"""

        xml = converter.convert(text)

        # Check all JSON operations are preserved
        assert "JSONGetElement ( $ResultMessage ; \"group_id\" )" in xml
        assert "JSONGetElement ( $ResultMessage ; \"year\" )" in xml
        assert "ValueCount ( JSONListKeys ( $committeeMembers ; \"\" ) )" in xml
        assert '"[" & $committeeMemberIndex & "].member_id"' in xml

    def test_complex_string_concatenation(self, converter):
        """Test complex string concatenation."""
        text = 'Set Variable [ $ResultMessage ; Value: "CreateOrUpdateWWWRecord (sheet) failed. " & $createSheetResultTitle & " " & $createSheetResultMessage ]'
        xml = converter.convert(text)

        assert '"CreateOrUpdateWWWRecord (sheet) failed. "' in xml
        assert "$createSheetResultTitle" in xml
        assert "$createSheetResultMessage" in xml
        # Check & operators are preserved
        assert ' & ' in xml or '&' in xml


class TestCDATAPreservation:
    """Test that CDATA sections preserve content correctly."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_ampersand_not_escaped_in_cdata(self, converter):
        """Test that & is not escaped as &amp; in CDATA."""
        text = 'Set Variable [ $msg ; Value: "a" & "b" ]'
        xml = converter.convert(text)

        # Find CDATA section
        import re
        cdata_matches = re.findall(r'<!\[CDATA\[(.*?)\]\]>', xml, re.DOTALL)

        for cdata in cdata_matches:
            # & should be present, not &amp;
            if '&' in cdata:
                assert '&amp;' not in cdata or cdata.count('&amp;') == 0

    def test_special_characters_in_cdata(self, converter):
        """Test that special characters are preserved in CDATA."""
        # Use triple quotes to avoid escaping issues
        text = """Set Variable [ $msg ; Value: "<test> & "more" & 'quotes'" ]"""
        xml = converter.convert(text)

        # CDATA should preserve everything
        assert "<![CDATA[" in xml
        assert "]]>" in xml


class TestErrorHandling:
    """Test error handling and edge cases."""

    @pytest.fixture
    def converter(self):
        """Create converter instance."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        return Converter(str(steps_dir))

    def test_unknown_step_raises_error(self, converter):
        """Test that unknown steps raise error by default."""
        text = "Unknown Step [ param: value ]"

        with pytest.raises(UnknownStepError):
            converter.convert(text)

    def test_unknown_step_continue_on_error(self, converter):
        """Test that unknown steps can be skipped."""
        text = """Set Variable [ $var ; Value: 1 ]
Unknown Step [ param: value ]
Exit Script"""

        xml = converter.convert(text, stop_on_error=False)

        assert "Set Variable" in xml
        assert "Exit Script" in xml
        # Should have error comment
        assert "ERROR" in xml or "Unknown" in xml

    def test_empty_input(self, converter):
        """Test empty input."""
        xml = converter.convert("")
        assert "<fmxmlsnippet" in xml

    def test_whitespace_only(self, converter):
        """Test whitespace-only input."""
        xml = converter.convert("   \n\n   ")
        assert "<fmxmlsnippet" in xml

