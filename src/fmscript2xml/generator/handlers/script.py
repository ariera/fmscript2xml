"""
Handlers for script execution steps: Perform Script, Install OnTimer Script.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import (
    create_step_element,
    create_cdata_element,
    create_helper_comment_step,
)
from .base import StepHandler


class PerformScriptHandler(StepHandler):
    """Handler for Perform Script steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        elements = []

        # Check if we need a helper comment
        needs_comment = False
        if 'Specified: From list' in step.raw_text:
            needs_comment = True
            comment_elem = create_helper_comment_step(step.raw_text)
            elements.append(comment_elem)

        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Script parameter (optional)
        param = step.params.get('Parameter', '')
        if param:
            calc_elem = create_cdata_element(param)
            step_elem.append(calc_elem)

            # DisplayCalculation
            display_elem = ET.Element('DisplayCalculation')
            display_calc = create_cdata_element(param)
            display_elem.append(display_calc)
            step_elem.append(display_elem)

        # Script name
        script_name = step.params.get('Script', step.params.get('0', ''))
        if script_name.startswith('"') and script_name.endswith('"'):
            script_name = script_name[1:-1]

        # Check if calculated
        if 'Calculated:' in step.raw_text or script_name.startswith('"'):
            # Calculated script name
            calc_elem = ET.Element('Calculated')
            calc_calc = create_cdata_element(script_name)
            calc_elem.append(calc_calc)
            step_elem.append(calc_elem)
        else:
            # Named script
            script_elem = ET.Element('Script')
            script_elem.set('name', script_name)
            script_elem.set('id', '1')  # Default ID (FileMaker will correct)
            step_elem.append(script_elem)

        elements.append(step_elem)
        return elements


class InstallOnTimerScriptHandler(StepHandler):
    """Handler for Install OnTimer Script steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Script name (positional 0)
        script_name = step.params.get('Script', step.params.get('0', ''))
        if script_name.startswith('"') and script_name.endswith('"'):
            script_name = script_name[1:-1]
        if script_name:
            script_elem = ET.Element('Script')
            script_elem.set('name', script_name)
            step_elem.append(script_elem)

        # Interval (positional 1)
        interval = step.params.get('Interval', step.params.get('1', ''))
        if interval:
            interval_elem = ET.Element('Interval')
            calc_elem = create_cdata_element(interval)
            interval_elem.append(calc_elem)
            step_elem.append(interval_elem)

        return [step_elem]
