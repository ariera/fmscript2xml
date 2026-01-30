"""
Parser for FileMaker script syntax.

Converts plain text into structured ParsedStep objects.
"""

import re
from typing import List, Optional, Dict, Any
from dataclasses import dataclass, field


@dataclass
class ParsedStep:
    """Represents a parsed FileMaker script step."""

    name: str
    params: Dict[str, Any] = field(default_factory=dict)
    raw_text: str = ""
    line_number: int = 0
    is_comment: bool = False
    comment_text: str = ""
    is_disabled: bool = False


class Parser:
    """
    Parses plain text FileMaker script steps.

    Handles:
    - Step name extraction
    - Parameter parsing (brackets, semicolons, key-value pairs)
    - Calculation preservation
    - Nested brackets
    - Comments
    """

    def __init__(self):
        self.steps: List[ParsedStep] = []

    def parse(self, text: str) -> List[ParsedStep]:
        """
        Parse plain text into list of ParsedStep objects.

        Args:
            text: Plain text FileMaker script

        Returns:
            List of ParsedStep objects
        """
        lines = text.split('\n')
        self.steps = []

        i = 0
        while i < len(lines):
            line_num = i + 1
            line = lines[i].strip()

            # Skip empty lines
            if not line:
                i += 1
                continue

            # Comments - preserve indentation
            if line.startswith('#'):
                # Preserve leading whitespace before the #
                # Find the position of # in the original line
                original_line = lines[i]
                hash_pos = original_line.find('#')
                leading_whitespace = original_line[:hash_pos]
                comment_text = original_line[hash_pos + 1:]  # Everything after #

                step = ParsedStep(
                    name="Comment",
                    is_comment=True,
                    comment_text=comment_text,  # Don't strip - preserve indentation after #
                    raw_text=original_line,  # Preserve original line
                    line_number=line_num
                )
                self.steps.append(step)
                i += 1
                continue

            # Disabled steps (// prefix) - FileMaker uses // to mark disabled steps
            is_disabled = False
            if line.startswith('//'):
                is_disabled = True
                # Remove // prefix and any following whitespace
                line = line[2:].strip()
                # Also update the original line for raw_text
                original_line = lines[i]
                if original_line.strip().startswith('//'):
                    # Find the position of // in the original line
                    double_slash_pos = original_line.find('//')
                    # Keep the // in raw_text but remove it from the parsed line
                    original_line = original_line[:double_slash_pos] + original_line[double_slash_pos + 2:].lstrip()
                if not line:
                    # Line was just // with nothing after - skip it
                    i += 1
                    continue

            # Check if this looks like a continuation line (starts with closing bracket/paren)
            # or doesn't have alphabetic characters in first part
            if line.startswith((']', ')')) or (not any(c.isalpha() for c in line[:20]) and '[' not in line and not line[0].isupper()):
                # This is likely a continuation line - skip it
                i += 1
                continue

            # Check for ellipsis truncation marker - if found, truncate the line at that point
            # This handles files that have been truncated with … marker
            if '…' in line:
                # Truncate at ellipsis and try to close any open brackets
                ellipsis_pos = line.find('…')
                truncated_line = line[:ellipsis_pos].strip()

                # Try to close brackets if needed
                open_brackets = truncated_line.count('[') - truncated_line.count(']')
                if open_brackets > 0:
                    # Add closing brackets
                    truncated_line += ']' * open_brackets

                line = truncated_line
                # Continue parsing this truncated line as a step

            # Try to parse as a step
            # If it has an opening bracket, collect continuation lines until brackets are balanced
            full_line = line
            if '[' in line:
                bracket_count = line.count('[') - line.count(']')
                j = i + 1
                while bracket_count > 0 and j < len(lines):
                    next_line = lines[j].strip()
                    # Skip lines with ellipsis (they're truncated)
                    if '…' in next_line:
                        # Truncate and try to close brackets
                        ellipsis_pos = next_line.find('…')
                        next_line = next_line[:ellipsis_pos].strip()
                        # Close any remaining brackets
                        remaining_brackets = bracket_count - (next_line.count('[') - next_line.count(']'))
                        if remaining_brackets > 0:
                            next_line += ']' * remaining_brackets
                            bracket_count = 0
                        else:
                            bracket_count += next_line.count('[') - next_line.count(']')

                    if next_line:  # Skip empty continuation lines
                        full_line += ' ' + next_line
                        bracket_count += next_line.count('[') - next_line.count(']')
                    j += 1
                    if bracket_count <= 0:
                        break
                i = j
            else:
                i += 1

            # Parse the (possibly multi-line) step
            step = self._parse_step(full_line, line_num)
            if step:
                # Mark as disabled if // prefix was detected
                step.is_disabled = is_disabled
                # Only add if step has a valid name (not empty)
                if step.name.strip():
                    self.steps.append(step)

        return self.steps

    def _parse_step(self, line: str, line_num: int) -> Optional[ParsedStep]:
        """Parse a single step line."""
        # Find step name (everything before '[' or end of line)
        bracket_pos = line.find('[')

        if bracket_pos == -1:
            # No parameters - step name only
            step_name = line.strip()
            return ParsedStep(
                name=step_name,
                raw_text=line,
                line_number=line_num
            )

        # Extract step name
        step_name = line[:bracket_pos].strip()

        # Extract parameters (everything between brackets)
        params_text = self._extract_bracketed_content(line, bracket_pos)

        # Parse parameters
        params = self._parse_params(params_text)

        return ParsedStep(
            name=step_name,
            params=params,
            raw_text=line,
            line_number=line_num
        )

    def _extract_bracketed_content(self, text: str, start_pos: int) -> str:
        """
        Extract content between matching brackets, handling nested brackets.

        Args:
            text: Full text
            start_pos: Position of opening bracket

        Returns:
            Content between brackets (without the brackets themselves)
        """
        if start_pos >= len(text) or text[start_pos] != '[':
            return ""

        depth = 0
        pos = start_pos

        while pos < len(text):
            if text[pos] == '[':
                depth += 1
            elif text[pos] == ']':
                depth -= 1
                if depth == 0:
                    # Found matching closing bracket
                    return text[start_pos + 1:pos].strip()
            pos += 1

        # No closing bracket found - return everything after opening bracket
        return text[start_pos + 1:].strip()

    def _parse_params(self, params_text: str) -> Dict[str, Any]:
        """
        Parse parameter string into dictionary.

        Parameters can be:
        - Key-value pairs: "Key: Value"
        - Standalone values: "Value"
        - Multiple parameters separated by semicolons

        Args:
            params_text: Parameter text (without brackets)

        Returns:
            Dictionary of parameters
        """
        if not params_text:
            return {}

        params = {}

        # Split by semicolons, but be careful with semicolons inside calculations
        parts = self._smart_split(params_text, ';')

        for part in parts:
            part = part.strip()
            if not part:
                continue

            # Check if it's a key-value pair
            # Look for colon, but skip :: (table reference separator in FileMaker)
            # and colons inside quoted strings
            colon_pos = -1
            i = 0
            in_string = False
            string_char = None
            while i < len(part):
                char = part[i]

                # Handle string literals
                if char in ('"', "'") and (i == 0 or part[i - 1] != '\\'):
                    if not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char:
                        in_string = False
                        string_char = None
                    i += 1
                    continue

                if in_string:
                    i += 1
                    continue

                if char == ':':
                    # Check if it's :: (table reference) or single : (parameter separator)
                    if i + 1 < len(part) and part[i + 1] == ':':
                        # Skip :: (table reference)
                        i += 2
                        continue
                    else:
                        # Found single colon - this is a parameter separator
                        colon_pos = i
                        break
                i += 1

            if colon_pos != -1:
                key = part[:colon_pos].strip()
                value = part[colon_pos + 1:].strip()

                # DON'T remove quotes - preserve them for calculations
                # Calculations need to keep their string literals intact
                # Only remove outer quotes if it's a simple standalone string (not a calculation)
                # For now, preserve all quotes to maintain calculation integrity
                params[key] = value
            else:
                # Standalone value - store as positional parameter
                # Use index as key
                positional_index = len([k for k in params.keys() if k.isdigit()])
                params[str(positional_index)] = part

        return params

    def _smart_split(self, text: str, delimiter: str) -> List[str]:
        """
        Split text by delimiter, but don't split inside brackets, parentheses, or quotes.

        Args:
            text: Text to split
            delimiter: Delimiter character

        Returns:
            List of parts
        """
        parts = []
        current_part = []
        bracket_depth = 0
        paren_depth = 0
        in_string = False
        string_char = None
        i = 0

        while i < len(text):
            char = text[i]

            # Handle string literals
            if char in ('"', "'") and (i == 0 or text[i - 1] != '\\'):
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                    string_char = None
                current_part.append(char)
                i += 1
                continue

            if in_string:
                current_part.append(char)
                i += 1
                continue

            # Handle brackets
            if char == '[':
                bracket_depth += 1
                current_part.append(char)
            elif char == ']':
                bracket_depth -= 1
                current_part.append(char)
            # Handle parentheses (for function calls)
            elif char == '(':
                paren_depth += 1
                current_part.append(char)
            elif char == ')':
                paren_depth -= 1
                current_part.append(char)
            elif char == delimiter and bracket_depth == 0 and paren_depth == 0:
                # Found delimiter at top level (not inside brackets, parens, or strings)
                parts.append(''.join(current_part))
                current_part = []
            else:
                current_part.append(char)

            i += 1

        # Add remaining part
        if current_part:
            parts.append(''.join(current_part))

        return parts

