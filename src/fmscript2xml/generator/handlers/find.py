"""
Handler for Perform Find steps.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_helper_comment_step
from .base import StepHandler


class PerformFindHandler(StepHandler):
    """Handler for Perform Find steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        elements = []

        # Add helper comment (find steps reference fields which need IDs)
        comment_elem = create_helper_comment_step(step.raw_text)
        elements.append(comment_elem)

        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Restore state - only add if explicitly specified or if there are other params
        # If params are empty (Perform Find []), don't add Restore
        restore = step.params.get('Restore', '')
        if restore:
            # Restore was explicitly specified
            restore_state = 'True' if restore.lower() != 'false' else 'False'
            restore_elem = ET.Element('Restore')
            restore_elem.set('state', restore_state)
            step_elem.append(restore_elem)
        elif step.params:
            # There are other params but no Restore specified - default to True
            restore_elem = ET.Element('Restore')
            restore_elem.set('state', 'True')
            step_elem.append(restore_elem)
        # If params are empty, don't add Restore element

        # Query structure (simplified - real implementation would parse find criteria)
        # Only add query if parameters are provided
        if step.params:
            query_elem = ET.Element('Query')
            query_elem.set('table', step.params.get('Table', ''))

            # RequestRow (simplified)
            request_elem = ET.Element('RequestRow')
            request_elem.set('operation', 'Include')

            # Criteria would be parsed from parameters
            # For MVP, just create empty structure
            query_elem.append(request_elem)
            step_elem.append(query_elem)

        elements.append(step_elem)
        return elements
