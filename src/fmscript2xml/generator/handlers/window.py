"""
Handlers for window-related steps: New Window, Close Window, Enter Preview Mode.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_cdata_element
from .base import StepHandler


class NewWindowHandler(StepHandler):
    """Handler for New Window steps."""

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

        # LayoutDestination - default to CurrentLayout
        dest_elem = ET.Element('LayoutDestination')
        dest_elem.set('value', 'CurrentLayout')
        step_elem.append(dest_elem)

        # Window Name (wrapped in Calculation)
        window_name = step.params.get('Name', '')
        if window_name:
            name_elem = ET.Element('Name')
            calc_elem = create_cdata_element(window_name)
            name_elem.append(calc_elem)
            step_elem.append(name_elem)

        # Height (wrapped in Calculation)
        height = step.params.get('Height', '')
        if height:
            height_elem = ET.Element('Height')
            calc_elem = create_cdata_element(height)
            height_elem.append(calc_elem)
            step_elem.append(height_elem)

        # Width (wrapped in Calculation)
        width = step.params.get('Width', '')
        if width:
            width_elem = ET.Element('Width')
            calc_elem = create_cdata_element(width)
            width_elem.append(calc_elem)
            step_elem.append(width_elem)

        # DistanceFromTop (formerly Top - wrapped in Calculation)
        top = step.params.get('Top', '')
        if top:
            top_elem = ET.Element('DistanceFromTop')
            calc_elem = create_cdata_element(top)
            top_elem.append(calc_elem)
            step_elem.append(top_elem)

        # DistanceFromLeft (formerly Left - wrapped in Calculation)
        left = step.params.get('Left', '')
        if left:
            left_elem = ET.Element('DistanceFromLeft')
            calc_elem = create_cdata_element(left)
            left_elem.append(calc_elem)
            step_elem.append(left_elem)

        # NewWndStyles - parse from Style parameter
        # Style values: (Style attr, Close, Minimize, Maximize, Resize, Styles bitmask)
        style = step.params.get('Style', 'Document')
        style_map = {
            'Document': ('Document', 'Yes', 'Yes', 'Yes', 'Yes', '0'),
            'Floating Document': ('Floating', 'Yes', 'No', 'No', 'Yes', '2147549952'),
            'Dialog': ('Dialog', 'Yes', 'No', 'Yes', 'Yes', '0'),
            'Card': ('Card', 'Yes', 'No', 'No', 'No', '0'),
        }

        style_info = style_map.get(style, style_map['Document'])
        styles_elem = ET.Element('NewWndStyles')
        styles_elem.set('Style', style_info[0])
        styles_elem.set('Close', style_info[1])
        styles_elem.set('Minimize', style_info[2])
        styles_elem.set('Maximize', style_info[3])
        styles_elem.set('Resize', style_info[4])
        styles_elem.set('Styles', style_info[5])
        step_elem.append(styles_elem)

        return [step_elem]


class CloseWindowHandler(StepHandler):
    """Handler for Close Window steps."""

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

        # LimitToWindowsOfCurrentFile - default to True
        limit_elem = ET.Element('LimitToWindowsOfCurrentFile')
        limit_elem.set('state', 'True')
        step_elem.append(limit_elem)

        # Window value - check if it's "Current Window" or a named window
        window_value = step.params.get('0', 'Current Window')
        if not window_value:
            window_value = 'Current Window'

        if window_value.lower() == 'current window' or window_value.lower() == 'current':
            # Current Window
            window_elem = ET.Element('Window')
            window_elem.set('value', 'Current')
            step_elem.append(window_elem)
        else:
            # Named window - use ByName with Calculation
            window_elem = ET.Element('Window')
            window_elem.set('value', 'ByName')
            step_elem.append(window_elem)

            name_elem = ET.Element('Name')
            calc_elem = create_cdata_element(window_value)
            name_elem.append(calc_elem)
            step_elem.append(name_elem)

        return [step_elem]


class EnterPreviewModeHandler(StepHandler):
    """Handler for Enter Preview Mode steps."""

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

        # Pause state - "On"/"Off" -> "True"/"False"
        pause_value = step.params.get('Pause', 'Off')
        pause_state = 'True' if pause_value.lower() == 'on' else 'False'

        pause_elem = ET.Element('Pause')
        pause_elem.set('state', pause_state)
        step_elem.append(pause_elem)

        return [step_elem]
