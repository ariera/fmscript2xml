"""
Handlers for control flow steps: If, Else If, Else, End If, Exit Script.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_cdata_element
from .base import StepHandler


class IfHandler(StepHandler):
    """Handler for If steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Calculation (condition)
        calc = step.params.get('Calculation', step.params.get('0', ''))
        if not calc and step.params:
            # Try to get first param as calculation
            calc = list(step.params.values())[0]

        calc_elem = create_cdata_element(calc)
        step_elem.append(calc_elem)

        return [step_elem]


class ElseIfHandler(StepHandler):
    """Handler for Else If steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Calculation (condition) - same as If
        calc = step.params.get('Calculation', step.params.get('0', ''))
        if not calc and step.params:
            # Try to get first param as calculation
            calc = list(step.params.values())[0]

        calc_elem = create_cdata_element(calc)
        step_elem.append(calc_elem)

        return [step_elem]


class ElseHandler(StepHandler):
    """Handler for Else steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )
        return [step_elem]


class EndIfHandler(StepHandler):
    """Handler for End If steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )
        return [step_elem]


class ExitScriptHandler(StepHandler):
    """Handler for Exit Script steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Text Result (optional)
        # Try multiple parameter names - check both with and without space
        text_result = (step.params.get('Text Result') or
                      step.params.get('TextResult') or
                      step.params.get('Result') or
                      step.params.get('0', ''))

        # If not found in params, try to extract from raw text
        if not text_result and step.raw_text:
            import re
            # Look for "Text Result: value" pattern
            match = re.search(r'Text Result:\s*(.+?)(?:\s*\]|$)', step.raw_text)
            if match:
                text_result = match.group(1).strip()

        if text_result:
            # Calculation should be direct child of Step, not wrapped in TextResult
            # Preserve the calculation exactly as written
            calc_elem = create_cdata_element(text_result)
            step_elem.append(calc_elem)

        return [step_elem]
