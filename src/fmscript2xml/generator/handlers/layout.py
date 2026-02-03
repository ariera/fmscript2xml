"""
Handlers for layout navigation steps: Go to Layout, Go to Record/Request/Page, Go to Related Record.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import (
    create_step_element,
    create_cdata_element,
    create_layout_element,
    create_table_element,
    create_helper_comment_step,
)
from .base import StepHandler


class GoToLayoutHandler(StepHandler):
    """Handler for Go to Layout steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        elements = []

        # Add helper comment for layout steps (they need IDs for named layouts)
        comment_elem = create_helper_comment_step(step.raw_text)
        elements.append(comment_elem)

        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Layout name/calculation
        layout_name = step.params.get('Layout', step.params.get('0', ''))

        # Check if it's a calculation (variable, function call, etc.)
        is_calculated = (
            layout_name.startswith('$') or  # Variable
            '(' in layout_name or  # Function call
            '&' in layout_name or  # Concatenation
            '=' in layout_name or  # Comparison
            not (layout_name.startswith('"') and layout_name.endswith('"'))  # Not a simple string
        )

        if is_calculated:
            # Use Layout element with Calculation inside
            dest_elem = ET.Element('LayoutDestination')
            dest_elem.set('value', 'LayoutNameByCalc')
            step_elem.append(dest_elem)

            # Layout element with Calculation inside
            layout_elem = ET.Element('Layout')
            layout_calc = create_cdata_element(layout_name)
            layout_elem.append(layout_calc)
            step_elem.append(layout_elem)
        else:
            # Named layout
            dest_elem = ET.Element('LayoutDestination')
            dest_elem.set('value', 'SelectedLayout')
            step_elem.append(dest_elem)

            # Remove quotes if present
            if layout_name.startswith('"') and layout_name.endswith('"'):
                layout_name = layout_name[1:-1]

            layout_elem = create_layout_element(layout_name, omit_id=True)
            step_elem.append(layout_elem)

        # Animation (optional)
        animation = step.params.get('Animation', '')
        if animation and animation != 'None':
            anim_elem = ET.Element('Animation')
            anim_elem.set('value', animation)
            step_elem.append(anim_elem)

        elements.append(step_elem)
        return elements


class GoToRecordRequestPageHandler(StepHandler):
    """Handler for Go to Record/Request/Page steps."""

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

        # NoInteract - "With dialog: On/Off" -> state="False/True"
        with_dialog = step.params.get('With dialog', 'On')
        no_interact_elem = ET.Element('NoInteract')
        no_interact_elem.set('state', 'True' if with_dialog.lower() == 'off' else 'False')
        step_elem.append(no_interact_elem)

        # Exit after last (only relevant for Next/Previous when specified)
        exit_after_last = step.params.get('Exit after last')
        if exit_after_last is not None:
            exit_elem = ET.Element('Exit')
            exit_elem.set('state', 'True' if exit_after_last.lower() == 'on' else 'False')
            step_elem.append(exit_elem)

        # Row/Page location
        location_value = step.params.get('0', '')
        calc_value = ''
        if 'With dialog' in step.params:
            calc_value = location_value
            location_value = 'ByCalculation'
        elif location_value and location_value not in {'First', 'Last', 'Next', 'Previous'}:
            calc_value = location_value
            location_value = 'ByCalculation'

        if not location_value:
            location_value = 'First'

        location_elem = ET.Element('RowPageLocation')
        location_elem.set('value', location_value)
        step_elem.append(location_elem)

        if location_value == 'ByCalculation' and calc_value:
            calc_elem = create_cdata_element(calc_value)
            step_elem.append(calc_elem)

        return [step_elem]


class GoToRelatedRecordHandler(StepHandler):
    """Handler for Go to Related Record steps."""

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

        # Option / MatchAllRecords / ShowInNewWindow / Restore
        option_state = 'False'
        match_all_state = 'False'
        show_new_window_state = 'False'

        option_text = step.params.get('0', '')
        if option_text:
            lowered = option_text.lower()
            if 'show all' in lowered:
                match_all_state = 'True'
            if 'show in new window' in lowered:
                show_new_window_state = 'True'
            if 'show only related' in lowered:
                option_state = 'False'

        option_elem = ET.Element('Option')
        option_elem.set('state', option_state)
        step_elem.append(option_elem)

        match_elem = ET.Element('MatchAllRecords')
        match_elem.set('state', match_all_state)
        step_elem.append(match_elem)

        show_elem = ET.Element('ShowInNewWindow')
        show_elem.set('state', show_new_window_state)
        step_elem.append(show_elem)

        restore_elem = ET.Element('Restore')
        restore_elem.set('state', 'True')
        step_elem.append(restore_elem)

        # LayoutDestination and Layout (layout appended after Table for ordering)
        layout_value = step.params.get('Using layout', step.params.get('Layout', ''))
        layout_elem = None
        if layout_value:
            is_calculated = (
                layout_value.startswith('$') or
                '(' in layout_value or
                '&' in layout_value or
                '=' in layout_value or
                not (layout_value.startswith('"') and layout_value.endswith('"'))
            )
            dest_elem = ET.Element('LayoutDestination')
            dest_elem.set('value', 'LayoutNameByCalc' if is_calculated else 'SelectedLayout')
            step_elem.append(dest_elem)

            if is_calculated:
                layout_elem = ET.Element('Layout')
                layout_calc = create_cdata_element(layout_value)
                layout_elem.append(layout_calc)
            else:
                layout_name = layout_value[1:-1]
                layout_elem = create_layout_element(layout_name, omit_id=True)

        # Name element (used for display/external layout state)
        if option_text:
            name_elem = ET.Element('Name')
            calc_elem = create_cdata_element(f"/*{option_text}*/")
            name_elem.append(calc_elem)
            step_elem.append(name_elem)

        # New window styles (default Document)
        styles_elem = ET.Element('NewWndStyles')
        styles_elem.set('Style', 'Document')
        styles_elem.set('Close', 'Yes')
        styles_elem.set('Minimize', 'Yes')
        styles_elem.set('Maximize', 'Yes')
        styles_elem.set('Resize', 'Yes')
        step_elem.append(styles_elem)

        # Table reference
        table_value = step.params.get('From table', step.params.get('Table', ''))
        if table_value:
            # Strip both straight quotes (") and curly quotes ("")
            # U+0022 = straight quote "
            # U+201C = left curly quote "
            # U+201D = right curly quote "
            if table_value.startswith('"') and table_value.endswith('"'):
                table_value = table_value[1:-1]
            elif table_value.startswith('\u201c') and table_value.endswith('\u201d'):
                table_value = table_value[1:-1]
            step_elem.append(create_table_element(table_value, omit_id=True))

        if layout_elem is not None:
            step_elem.append(layout_elem)

        return [step_elem]
