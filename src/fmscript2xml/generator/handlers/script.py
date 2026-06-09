"""
Handlers for script execution steps: Perform Script, Install OnTimer Script,
Perform Script on Server, Perform Script on Server with Callback.
"""

from typing import List, Optional, Tuple
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import (
    create_step_element,
    create_cdata_element,
    create_helper_comment_step,
)
from .base import StepHandler


def _strip_quotes(value: str) -> str:
    """Strip surrounding straight or curly (smart) quotes from a value."""
    value = value.strip()
    if len(value) >= 2:
        if value[0] == '"' and value[-1] == '"':
            return value[1:-1]
        if value[0] == '“' and value[-1] == '”':
            return value[1:-1]
    return value


def _is_calculated_script(specified: str, name: str) -> bool:
    """Determine whether a script reference is calculated (vs. named from list)."""
    if specified and 'by name' in specified.lower():
        return True
    name = name.strip()
    # A variable or unquoted calculation reference is calculated.
    if name.startswith('$'):
        return True
    return False


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


class PerformScriptOnServerHandler(StepHandler):
    """Handler for Perform Script on Server steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        elements = []

        # Named scripts (From list) need DB IDs we can't resolve; emit a helper
        # comment for manual reference, like Perform Script / Go to Layout.
        if 'from list' in step.raw_text.lower():
            elements.append(create_helper_comment_step(step.raw_text))

        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Wait for completion -> WaitForCompletion state
        wait = step.params.get('Wait for completion', 'Off')
        wait_elem = ET.Element('WaitForCompletion')
        wait_elem.set('state', 'True' if wait.strip().lower() == 'on' else 'False')
        step_elem.append(wait_elem)

        # Script parameter -> Calculation
        param = step.params.get('Parameter', '')
        if param:
            step_elem.append(create_cdata_element(param))

        # Script reference (named from list, or calculated by name)
        specified = step.params.get('Specified', '')
        script_name = step.params.get('Script', step.params.get('0', ''))
        if _is_calculated_script(specified, script_name):
            calc_elem = ET.Element('Calculated')
            calc_elem.append(create_cdata_element(script_name.strip()))
            step_elem.append(calc_elem)
        elif script_name:
            script_elem = ET.Element('Script')
            script_elem.set('name', _strip_quotes(script_name))
            step_elem.append(script_elem)

        elements.append(step_elem)
        return elements


class PerformScriptOnServerWithCallbackHandler(StepHandler):
    """Handler for Perform Script on Server with Callback steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        elements = []

        # Named scripts (From list) need DB IDs we can't resolve; emit a helper
        # comment for manual reference, like Perform Script / Go to Layout.
        if 'from list' in step.raw_text.lower():
            elements.append(create_helper_comment_step(step.raw_text))

        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # The two "Parameter:" keys collide in the parser's dict, so re-parse the
        # bracketed content in order and split it at the callback boundary.
        main_parts, callback_parts = self._split_sections(step.raw_text)
        main_spec, main_name, main_param, _ = self._parse_section(main_parts)
        cb_spec, cb_name, cb_param, state = self._parse_section(callback_parts)

        main_calculated = _is_calculated_script(main_spec, main_name)
        cb_calculated = _is_calculated_script(cb_spec, cb_name)

        # 1. Calculated main script name appears first (before CallbackScriptState).
        if main_calculated and main_name:
            calc_elem = ET.Element('Calculated')
            calc_elem.append(create_cdata_element(main_name.strip()))
            step_elem.append(calc_elem)

        # 2. CallbackScriptState
        if state:
            state_elem = ET.Element('CallbackScriptState')
            state_elem.set('value', state.strip())
            step_elem.append(state_elem)

        # 3. Main script parameter -> Calculation
        if main_param:
            step_elem.append(create_cdata_element(main_param))

        # 4. Named main script -> Script (after the parameter)
        if not main_calculated and main_name:
            script_elem = ET.Element('Script')
            script_elem.set('name', _strip_quotes(main_name))
            step_elem.append(script_elem)

        # 5. CallbackScript wrapper
        callback_elem = ET.Element('CallbackScript')
        if cb_calculated and cb_name:
            calc_elem = ET.Element('Calculated')
            calc_elem.append(create_cdata_element(cb_name.strip()))
            callback_elem.append(calc_elem)
        elif cb_name:
            name_elem = ET.Element('ScriptName')
            name_elem.set('name', _strip_quotes(cb_name))
            callback_elem.append(name_elem)

        if cb_param:
            sp_elem = ET.Element('ScriptParameter')
            sp_elem.append(create_cdata_element(cb_param))
            callback_elem.append(sp_elem)

        step_elem.append(callback_elem)

        elements.append(step_elem)
        return elements

    def _split_sections(self, raw_text: str) -> Tuple[List[str], List[str]]:
        """Split the bracketed content into main and callback part lists."""
        start = raw_text.find('[')
        end = raw_text.rfind(']')
        if start == -1 or end == -1 or end <= start:
            return [], []
        content = raw_text[start + 1:end]

        parts = self._split_top_level(content)
        main_parts: List[str] = []
        callback_parts: List[str] = []
        in_callback = False
        for part in parts:
            key, _ = self._split_kv(part)
            if key and key.strip().lower() == 'callback script specified':
                in_callback = True
            (callback_parts if in_callback else main_parts).append(part)
        return main_parts, callback_parts

    def _parse_section(
        self,
        parts: List[str]
    ) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
        """Extract (specified, script_name, parameter, state) from a section."""
        specified = name = parameter = state = None
        for part in parts:
            key, value = self._split_kv(part)
            if key is None:
                name = value
                continue
            key_lower = key.strip().lower()
            if key_lower in ('specified', 'callback script specified'):
                specified = value
            elif key_lower == 'parameter':
                parameter = value
            elif key_lower == 'state':
                state = value
        return specified, name, parameter, state

    @staticmethod
    def _split_top_level(text: str, delimiter: str = ';') -> List[str]:
        """Split on delimiter, ignoring delimiters inside brackets/parens/quotes."""
        parts: List[str] = []
        current: List[str] = []
        depth = 0
        in_string = False
        string_char = None
        for i, char in enumerate(text):
            if char in ('"', "'") and (i == 0 or text[i - 1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
                current.append(char)
                continue
            if in_string:
                current.append(char)
                continue
            if char in '([{':
                depth += 1
                current.append(char)
            elif char in ')]}':
                depth -= 1
                current.append(char)
            elif char == delimiter and depth == 0:
                parts.append(''.join(current))
                current = []
            else:
                current.append(char)
        if current:
            parts.append(''.join(current))
        return [p.strip() for p in parts if p.strip()]

    @staticmethod
    def _split_kv(part: str) -> Tuple[Optional[str], str]:
        """Split 'Key: Value' into (key, value); positional values return key None."""
        i = 0
        in_string = False
        string_char = None
        while i < len(part):
            char = part[i]
            if char in ('"', "'"):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
                i += 1
                continue
            if not in_string and char == ':':
                if i + 1 < len(part) and part[i + 1] == ':':
                    i += 2
                    continue
                return part[:i].strip(), part[i + 1:].strip()
            i += 1
        return None, part.strip()
