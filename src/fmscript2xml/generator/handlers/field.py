"""
Handlers for field-related steps: Set Field, Set Field By Name.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import (
    create_step_element,
    create_cdata_element,
    create_field_element,
    create_helper_comment_step,
)
from .base import StepHandler


class SetFieldHandler(StepHandler):
    """Handler for Set Field steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        elements = []

        # Create the Step element
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Field name (may be empty for "active field" usage)
        field_name = step.params.get('Field', '')
        value = step.params.get('Value', '')

        if not field_name:
            # If no explicit Field and only one positional param, treat it as the value
            if '0' in step.params and '1' not in step.params and not value:
                value = step.params.get('0', '')
            else:
                field_name = step.params.get('0', '')
                value = step.params.get('1', value)
        else:
            value = step.params.get('1', value)

        # Strip quotes from field name
        if field_name.startswith('"') and field_name.endswith('"'):
            field_name = field_name[1:-1]

        # FIRST: Add Calculation element as direct child (the value)
        calc_elem = create_cdata_element(value)
        step_elem.append(calc_elem)

        # SECOND: Add Field element (if field name is specified)
        if field_name:
            # Parse field name: Table::Field[repetition]
            table_name = None
            repetition = None

            # Check for repetition [n]
            import re
            repetition_match = re.search(r'\[(\d+)\]$', field_name)
            if repetition_match:
                repetition = repetition_match.group(1)
                field_name = field_name[:repetition_match.start()]

            # Split table and field
            if '::' in field_name:
                table_name, field_name = field_name.split('::', 1)

            field_elem = create_field_element(
                field_name,
                table_name=table_name,
                repetition=repetition,
                omit_id=True
            )
            step_elem.append(field_elem)

        elements.append(step_elem)
        return elements


class SetFieldByNameHandler(StepHandler):
    """Handler for Set Field By Name steps."""

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

        # First parameter: TargetName (field name calculation)
        target_name = step.params.get('0', '')
        if target_name:
            target_elem = ET.Element('TargetName')
            calc_elem = create_cdata_element(target_name)
            target_elem.append(calc_elem)
            step_elem.append(target_elem)

        # Second parameter: Result (value calculation)
        result = step.params.get('1', '')
        if result:
            result_elem = ET.Element('Result')
            calc_elem = create_cdata_element(result)
            result_elem.append(calc_elem)
            step_elem.append(result_elem)

        return [step_elem]
