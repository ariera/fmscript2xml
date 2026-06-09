"""
Handler for Show Custom Dialog steps.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_cdata_element, create_field_element, create_helper_comment_step
from .base import StepHandler


class ShowCustomDialogHandler(StepHandler):
    """Handler for Show Custom Dialog steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        elements = []

        # Add helper comment (dialog may reference fields which need IDs)
        if 'Field' in str(step.params):
            comment_elem = create_helper_comment_step(step.raw_text)
            elements.append(comment_elem)

        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            step_def['enable_default']
        )

        # Title
        title = step.params.get('Title', step.params.get('0', ''))
        if title:
            title_elem = ET.Element('Title')
            calc_elem = create_cdata_element(title)
            title_elem.append(calc_elem)
            step_elem.append(title_elem)

        # Message
        message = step.params.get('Message', step.params.get('1', ''))
        if message:
            msg_elem = ET.Element('Message')
            calc_elem = create_cdata_element(message)
            msg_elem.append(calc_elem)
            step_elem.append(msg_elem)

        # Buttons: always three. Button 1 commits (CommitState="True"); buttons
        # 2 and 3 do not. Defaults match FileMaker: "OK", "Cancel", and an empty
        # third button (rendered as a self-closing <Button>).
        button1 = step.params.get('Default Button', '"OK"')
        button2 = step.params.get('Button 2', '"Cancel"')
        button3 = step.params.get('Button 3', '')

        buttons_elem = ET.Element('Buttons')
        for btn_text, commit_state in (
            (button1, 'True'),
            (button2, 'False'),
            (button3, 'False'),
        ):
            btn_elem = ET.Element('Button')
            btn_elem.set('CommitState', commit_state)
            if btn_text:
                btn_elem.append(create_cdata_element(btn_text))
            buttons_elem.append(btn_elem)
        step_elem.append(buttons_elem)

        # InputFields (simplified - would parse field list)
        input_fields = step.params.get('InputFields', '')
        if input_fields:
            fields_elem = ET.Element('InputFields')
            # Parse field list (simplified)
            field_list = input_fields.split(',') if ',' in input_fields else [input_fields]
            for field_name in field_list:
                field_elem = ET.Element('InputField')
                field_ref = create_field_element(field_name.strip(), omit_id=True)
                field_elem.append(field_ref)
                fields_elem.append(field_elem)
            step_elem.append(fields_elem)

        elements.append(step_elem)
        return elements
