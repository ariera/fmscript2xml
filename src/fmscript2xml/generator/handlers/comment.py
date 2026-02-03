"""
Handler for Comment steps.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_text_element
from .base import StepHandler


class CommentHandler(StepHandler):
    """Handler for Comment steps."""

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

        if step.is_comment:
            text = step.comment_text
        else:
            # Extract text from params
            text = step.params.get('Text', step.params.get('0', ''))

        text_elem = create_text_element('Text', text)
        step_elem.append(text_elem)

        return [step_elem]
