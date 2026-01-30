"""
Step-specific XML generation handlers.

Each handler knows how to convert a parsed step into XML
for a specific FileMaker script step type.
"""

from xml.etree import ElementTree as ET
from typing import List, Optional, Dict, Any
from ..parser.parser import ParsedStep
from ..registry.step_def import StepDefinition
from .xml_builder import (
    create_step_element,
    create_cdata_element,
    create_text_element,
    create_field_element,
    create_layout_element,
    create_table_element,
    create_helper_comment_step
)


class StepHandler:
    """Base class for step handlers."""

    def can_handle(self, step: ParsedStep, step_def: StepDefinition) -> bool:
        """Check if this handler can handle the given step."""
        return step.name == step_def.name

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        """
        Generate XML elements for this step.

        Returns:
            List of Step elements (may include helper comments)
        """
        raise NotImplementedError


class CommentHandler(StepHandler):
    """Handler for Comment steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
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


class SetVariableHandler(StepHandler):
    """Handler for Set Variable steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )

        # Variable name - PRESERVE the $ prefix
        # Try Name parameter first, then positional parameter 0
        var_name = step.params.get('Name', '')
        if not var_name:
            var_name = step.params.get('0', '')

        # If still not found or doesn't have $, try to extract from raw text
        if not var_name or (not var_name.startswith('$') and step.raw_text):
            import re
            # Look for $variable pattern in the raw text
            match = re.search(r'\$[a-zA-Z0-9_]+', step.raw_text)
            if match:
                var_name = match.group(0)

        # Ensure $ prefix is present (FileMaker requires it)
        if var_name and not var_name.startswith('$'):
            var_name = '$' + var_name

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

        # Name comes last (matching FileMaker's XML order)
        name_elem = create_text_element('Name', var_name)
        step_elem.append(name_elem)

        return [step_elem]


class IfHandler(StepHandler):
    """Handler for If steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
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
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
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
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )
        return [step_elem]


class SetErrorCaptureHandler(StepHandler):
    """Handler for Set Error Capture steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )

        # Get the state from params - "On" or "Off"
        state_value = step.params.get('0', 'On')
        if not state_value:
            state_value = 'On'  # Default to On

        # Convert "On"/"Off" to "True"/"False"
        state = 'True' if state_value.lower() == 'on' else 'False'

        # Use <Set state="True/False"/> structure
        set_elem = ET.Element('Set')
        set_elem.set('state', state)
        step_elem.append(set_elem)

        return [step_elem]


class NewWindowHandler(StepHandler):
    """Handler for New Window steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
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
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
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
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )

        # Pause state - "On"/"Off" -> "True"/"False"
        pause_value = step.params.get('Pause', 'Off')
        pause_state = 'True' if pause_value.lower() == 'on' else 'False'

        pause_elem = ET.Element('Pause')
        pause_elem.set('state', pause_state)
        step_elem.append(pause_elem)

        return [step_elem]


class PrintHandler(StepHandler):
    """Handler for Print steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )

        # NoInteract - "With dialog: On/Off" -> state="False/True"
        with_dialog = step.params.get('With dialog', 'On')
        no_interact_state = 'True' if with_dialog.lower() == 'off' else 'False'

        no_interact_elem = ET.Element('NoInteract')
        no_interact_elem.set('state', no_interact_state)
        step_elem.append(no_interact_elem)

        # Restore state - if "Restore" is present, state is True
        restore_value = step.params.get('Restore', '')
        restore_state = 'True' if restore_value else 'False'

        restore_elem = ET.Element('Restore')
        restore_elem.set('state', restore_state)
        step_elem.append(restore_elem)

        # Note: PrintSettings with PlatformData cannot be generated from text
        # FileMaker will use default print settings when pasted

        return [step_elem]


class EndIfHandler(StepHandler):
    """Handler for End If steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )
        return [step_elem]


class ExitScriptHandler(StepHandler):
    """Handler for Exit Script steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
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


class PerformScriptHandler(StepHandler):
    """Handler for Perform Script steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        elements = []

        # Check if we need a helper comment
        needs_comment = False
        if 'Specified: From list' in step.raw_text:
            needs_comment = True
            comment_elem = create_helper_comment_step(step.raw_text)
            elements.append(comment_elem)

        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
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


class GoToLayoutHandler(StepHandler):
    """Handler for Go to Layout steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        elements = []

        # Add helper comment for layout steps (they need IDs for named layouts)
        comment_elem = create_helper_comment_step(step.raw_text)
        elements.append(comment_elem)

        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
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


class SetFieldHandler(StepHandler):
    """Handler for Set Field steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        elements = []

        # Add helper comment if field reference (needs ID)
        if 'Field' in step.params or any('field' in k.lower() for k in step.params.keys()):
            comment_elem = create_helper_comment_step(step.raw_text)
            elements.append(comment_elem)

        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
        )

        # Field name
        field_name = step.params.get('Field', step.params.get('0', ''))
        if field_name.startswith('"') and field_name.endswith('"'):
            field_name = field_name[1:-1]

        field_elem = create_field_element(field_name, omit_id=True)
        step_elem.append(field_elem)

        # Value (calculation)
        value = step.params.get('Value', step.params.get('1', ''))
        rep_elem = ET.Element('Repetition')
        calc_elem = create_cdata_element(value)
        rep_elem.append(calc_elem)
        step_elem.append(rep_elem)

        elements.append(step_elem)
        return elements


class PerformFindHandler(StepHandler):
    """Handler for Perform Find steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        elements = []

        # Add helper comment (find steps reference fields which need IDs)
        comment_elem = create_helper_comment_step(step.raw_text)
        elements.append(comment_elem)

        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
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
        # For now, create a basic query structure
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


class ShowCustomDialogHandler(StepHandler):
    """Handler for Show Custom Dialog steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        elements = []

        # Add helper comment (dialog may reference fields which need IDs)
        if 'Field' in str(step.params):
            comment_elem = create_helper_comment_step(step.raw_text)
            elements.append(comment_elem)

        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
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

        # Buttons (simplified - would parse button list)
        buttons = step.params.get('Buttons', '')
        if buttons:
            buttons_elem = ET.Element('Buttons')
            # Parse button list (simplified)
            button_list = buttons.split(',') if ',' in buttons else [buttons]
            for i, btn_text in enumerate(button_list):
                btn_elem = ET.Element('Button')
                btn_elem.set('CommitState', 'True' if i == 0 else 'False')
                calc_elem = create_cdata_element(btn_text.strip())
                btn_elem.append(calc_elem)
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


class OpenURLHandler(StepHandler):
    """Handler for Open URL steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )

        # NoInteract element for "With dialog" option
        # "With dialog: Off" -> NoInteract state="True"
        # "With dialog: On" -> NoInteract state="False"
        with_dialog = step.params.get('With dialog', 'On')
        no_interact = ET.Element('NoInteract')
        no_interact.set('state', 'True' if with_dialog.lower() == 'off' else 'False')
        step_elem.append(no_interact)

        # URL calculation - get the positional parameter (the URL expression)
        url = step.params.get('0', '')
        if url:
            calc_elem = create_cdata_element(url)
            step_elem.append(calc_elem)

        return [step_elem]


class SendMailHandler(StepHandler):
    """Handler for Send Mail steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )

        # NoInteract element for "With dialog" option
        with_dialog = step.params.get('With dialog', 'On')
        no_interact = ET.Element('NoInteract')
        no_interact.set('state', 'True' if with_dialog.lower() == 'off' else 'False')
        step_elem.append(no_interact)

        # To field
        to_value = step.params.get('To', '')
        if to_value:
            to_elem = ET.Element('To')
            to_elem.set('UseFoundSet', 'False')
            calc_elem = create_cdata_element(to_value)
            to_elem.append(calc_elem)
            step_elem.append(to_elem)

        # CC field
        cc_value = step.params.get('CC', step.params.get('Cc', ''))
        if cc_value:
            cc_elem = ET.Element('Cc')
            cc_elem.set('UseFoundSet', 'False')
            calc_elem = create_cdata_element(cc_value)
            cc_elem.append(calc_elem)
            step_elem.append(cc_elem)

        # BCC field
        bcc_value = step.params.get('BCC', step.params.get('Bcc', ''))
        if bcc_value:
            bcc_elem = ET.Element('Bcc')
            bcc_elem.set('UseFoundSet', 'False')
            calc_elem = create_cdata_element(bcc_value)
            bcc_elem.append(calc_elem)
            step_elem.append(bcc_elem)

        # Subject field
        subject_value = step.params.get('Subject', '')
        if subject_value:
            subject_elem = ET.Element('Subject')
            calc_elem = create_cdata_element(subject_value)
            subject_elem.append(calc_elem)
            step_elem.append(subject_elem)

        # Message field
        message_value = step.params.get('Message', '')
        if message_value:
            message_elem = ET.Element('Message')
            calc_elem = create_cdata_element(message_value)
            message_elem.append(calc_elem)
            step_elem.append(message_elem)

        # MultipleEmails - default to False
        multiple_emails = ET.Element('MultipleEmails')
        multiple_emails.set('state', 'False')
        step_elem.append(multiple_emails)

        # SendViaSMTP - check if "Send via E-mail Client" or "Send via SMTP"
        # First positional param often indicates the send method
        send_method = step.params.get('0', '')
        send_via_smtp = ET.Element('SendViaSMTP')
        send_via_smtp.set('state', 'True' if 'smtp' in send_method.lower() else 'False')
        step_elem.append(send_via_smtp)

        # SMTP Encryption type - default
        smtp_encryption = ET.Element('SMTPEncryptionType')
        smtp_encryption.set('type', 'SMTPEncryptionNone')
        step_elem.append(smtp_encryption)

        # SMTP Authentication type - default
        smtp_auth = ET.Element('SMTPAuthenticationType')
        smtp_auth.set('type', 'SMTPAuthenticationNone')
        step_elem.append(smtp_auth)

        return [step_elem]


class SetFieldByNameHandler(StepHandler):
    """Handler for Set Field By Name steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
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


class CommitRecordsRequestsHandler(StepHandler):
    """Handler for Commit Records/Requests steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def.enable_default and not step.is_disabled
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            enabled
        )

        # NoInteract - "With dialog: On/Off" -> state="False/True"
        with_dialog = step.params.get('With dialog', 'On')
        no_interact_state = 'True' if with_dialog.lower() == 'off' else 'False'

        no_interact_elem = ET.Element('NoInteract')
        no_interact_elem.set('state', no_interact_state)
        step_elem.append(no_interact_elem)

        # Check for "Force Commit" option
        force_commit = step.params.get('0', '')
        if force_commit and 'force' in force_commit.lower():
            # Option state="true" for Force Commit
            option_elem = ET.Element('Option')
            option_elem.set('state', 'true')
            step_elem.append(option_elem)

            # ESSForceCommit state="True"
            ess_elem = ET.Element('ESSForceCommit')
            ess_elem.set('state', 'True')
            step_elem.append(ess_elem)

        return [step_elem]


# Registry of handlers
HANDLERS = {
    'Comment': CommentHandler(),
    'Set Variable': SetVariableHandler(),
    'Set Error Capture': SetErrorCaptureHandler(),
    'New Window': NewWindowHandler(),
    'Close Window': CloseWindowHandler(),
    'Enter Preview Mode': EnterPreviewModeHandler(),
    'Print': PrintHandler(),
    'If': IfHandler(),
    'Else If': ElseIfHandler(),
    'Else': ElseHandler(),
    'End If': EndIfHandler(),
    'Exit Script': ExitScriptHandler(),
    'Perform Script': PerformScriptHandler(),
    'Go to Layout': GoToLayoutHandler(),
    'Set Field': SetFieldHandler(),
    'Perform Find': PerformFindHandler(),
    'Show Custom Dialog': ShowCustomDialogHandler(),
    'Open URL': OpenURLHandler(),
    'Send Mail': SendMailHandler(),
    'Set Field By Name': SetFieldByNameHandler(),
    'Commit Records/Requests': CommitRecordsRequestsHandler(),
}


def get_handler(step_name: str) -> Optional[StepHandler]:
    """Get handler for step name."""
    return HANDLERS.get(step_name)


def generate_xml(
    step: ParsedStep,
    step_def: StepDefinition
) -> List[ET.Element]:
    """
    Generate XML for a parsed step using appropriate handler.

    Args:
        step: Parsed step
        step_def: Step definition

    Returns:
        List of XML elements (may include helper comments)
    """
    # Try to find specific handler
    handler = get_handler(step.name)

    if handler and handler.can_handle(step, step_def):
        return handler.generate(step, step_def)

    # Default handler: create basic step element
    # Check if step is disabled (// prefix)
    enabled = step_def.enable_default and not step.is_disabled
    step_elem = create_step_element(
        step_def.id,
        step_def.xml_step_name,
        enabled
    )

    # Add parameters as child elements (generic handling)
    for key, value in step.params.items():
        if key.isdigit():
            # Positional parameter - treat as calculation
            calc_elem = create_cdata_element(str(value))
            step_elem.append(calc_elem)
        else:
            # Named parameter - sanitize element name (XML element names cannot contain spaces)
            # Replace spaces with camelCase or remove them
            element_name = key.replace(' ', '')  # Simple approach: remove spaces
            # If empty after removing spaces, use a default name
            if not element_name:
                element_name = 'Parameter'
            param_elem = ET.Element(element_name)
            param_elem.text = str(value)
            step_elem.append(param_elem)

    return [step_elem]

