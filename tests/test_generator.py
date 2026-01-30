"""Tests for generator module."""

import pytest
from xml.etree import ElementTree as ET
from fmscript2xml.parser.parser import ParsedStep
from fmscript2xml.registry.step_def import StepDefinition
from fmscript2xml.generator.step_handlers import generate_xml
from fmscript2xml.generator.xml_builder import (
    create_step_element,
    create_cdata_element,
    create_comment_step
)


class TestXMLBuilder:
    """Test XML builder utilities."""

    def test_create_step_element(self):
        """Test creating a step element."""
        step = create_step_element(141, "Set Variable", True)

        assert step.tag == "Step"
        assert step.get("id") == "141"
        assert step.get("name") == "Set Variable"
        assert step.get("enable") == "True"

    def test_create_cdata_element(self):
        """Test creating a calculation element."""
        calc = create_cdata_element("Get ( FoundCount )")

        assert calc.tag == "Calculation"
        assert calc.text == "Get ( FoundCount )"

    def test_create_comment_step(self):
        """Test creating a comment step."""
        step = create_comment_step("Test comment")

        assert step.tag == "Step"
        assert step.get("id") == "89"
        assert step.get("name") == "Comment"
        assert len(step) == 1
        assert step[0].tag == "Text"
        assert step[0].text == "Test comment"


class TestStepHandlers:
    """Test step handlers."""

    def test_comment_handler(self):
        """Test Comment handler."""
        step = ParsedStep(
            name="Comment",
            is_comment=True,
            comment_text="Test comment"
        )
        step_def = StepDefinition(
            id=89,
            name="Comment",
            category="Miscellaneous"
        )

        elements = generate_xml(step, step_def)

        assert len(elements) == 1
        assert elements[0].tag == "Step"
        assert elements[0].get("name") == "Comment"

    def test_set_variable_handler(self):
        """Test Set Variable handler."""
        step = ParsedStep(
            name="Set Variable",
            params={"Name": "$var", "Value": "1"}
        )
        step_def = StepDefinition(
            id=141,
            name="Set Variable",
            category="Control"
        )

        elements = generate_xml(step, step_def)

        assert len(elements) == 1
        assert elements[0].tag == "Step"
        assert elements[0].get("name") == "Set Variable"

