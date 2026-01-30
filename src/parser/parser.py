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

        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue

            # Comments
            if line.startswith('#'):
                step = ParsedStep(
                    name="Comment",
                    is_comment=True,
                    comment_text=line[1:].strip(),
                    raw_text=line,
                    line_number=line_num
                )
                self.steps.append(step)
                continue

            # Parse step
            step = self._parse_step(line, line_num)
            if step:
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

                # Remove quotes from string values if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]

                params[key] = value
            else:
                # Standalone value - store as positional parameter
                # Use index as key
                positional_index = len([k for k in params.keys() if k.isdigit()])
                params[str(positional_index)] = part

        return params

    def _smart_split(self, text: str, delimiter: str) -> List[str]:
        """
        Split text by delimiter, but don't split inside brackets or quotes.

        Args:
            text: Text to split
            delimiter: Delimiter character

        Returns:
            List of parts
        """
        parts = []
        current_part = []
        depth = 0
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
                depth += 1
                current_part.append(char)
            elif char == ']':
                depth -= 1
                current_part.append(char)
            elif char == delimiter and depth == 0:
                # Found delimiter at top level
                parts.append(''.join(current_part))
                current_part = []
            else:
                current_part.append(char)

            i += 1

        # Add remaining part
        if current_part:
            parts.append(''.join(current_part))

        return parts

