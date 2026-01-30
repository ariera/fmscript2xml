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
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
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
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
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


class IfHandler(StepHandler):
    """Handler for If steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
        )

        # Calculation (condition)
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
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
        )
        return [step_elem]


class EndIfHandler(StepHandler):
    """Handler for End If steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
        )
        return [step_elem]


class ExitScriptHandler(StepHandler):
    """Handler for Exit Script steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: StepDefinition
    ) -> List[ET.Element]:
        step_elem = create_step_element(
            step_def.id,
            step_def.xml_step_name,
            step_def.enable_default
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

        # Restore state (default True)
        restore = step.params.get('Restore', 'True')
        if restore.lower() != 'false':
            restore_elem = ET.Element('Restore')
            restore_elem.set('state', 'True')
            step_elem.append(restore_elem)

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


# Registry of handlers
HANDLERS = {
    'Comment': CommentHandler(),
    'Set Variable': SetVariableHandler(),
    'If': IfHandler(),
    'Else': ElseHandler(),
    'End If': EndIfHandler(),
    'Exit Script': ExitScriptHandler(),
    'Perform Script': PerformScriptHandler(),
    'Go to Layout': GoToLayoutHandler(),
    'Set Field': SetFieldHandler(),
    'Perform Find': PerformFindHandler(),
    'Show Custom Dialog': ShowCustomDialogHandler(),
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
    step_elem = create_step_element(
        step_def.id,
        step_def.xml_step_name,
        step_def.enable_default
    )

    # Add parameters as child elements (generic handling)
    for key, value in step.params.items():
        if key.isdigit():
            # Positional parameter - treat as calculation
            calc_elem = create_cdata_element(str(value))
            step_elem.append(calc_elem)
        else:
            # Named parameter
            param_elem = ET.Element(key)
            param_elem.text = str(value)
            step_elem.append(param_elem)

    return [step_elem]

