"""
Handler for Set Variable steps.
"""

import re
from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_cdata_element, create_text_element
from .base import StepHandler


class SetVariableHandler(StepHandler):
    """Handler for Set Variable steps."""

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

        # Variable name - PRESERVE the $ prefix
        # Try Name parameter first, then positional parameter 0
        var_name = step.params.get('Name', '')
        if not var_name:
            var_name = step.params.get('0', '')

        # If still not found or doesn't have $, try to extract from raw text
        if not var_name or (not var_name.startswith('$') and step.raw_text):
            # Look for $variable pattern in the raw text
            match = re.search(r'\$[a-zA-Z0-9_]+', step.raw_text)
            if match:
                var_name = match.group(0)

        # Ensure $ prefix is present (FileMaker requires it)
        if var_name and not var_name.startswith('$'):
            var_name = '$' + var_name

        # Name element (must come first based on FileMaker's XML structure)
        name_elem = create_text_element('Name', var_name)
        step_elem.append(name_elem)

        # Value (calculation) - preserve exactly as written
        value = step.params.get('Value', step.params.get('1', ''))
        # If value is empty string, preserve it as ""
        if value == '':
            value = '""'

        value_elem = ET.Element('Value')
        calc_elem = create_cdata_element(value)
        value_elem.append(calc_elem)
        step_elem.append(value_elem)

        # Repetition (default to 1)
        repetition = step.params.get('Repetition', '1')
        rep_elem = ET.Element('Repetition')
        rep_calc = create_cdata_element(repetition)
        rep_elem.append(rep_calc)
        step_elem.append(rep_elem)

        return [step_elem]
