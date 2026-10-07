"""
Parser for FileMaker script syntax.

Converts plain text into structured ParsedStep objects.
"""

import re
from typing import Iterator, List, Optional, Dict, Any, Tuple
from dataclasses import dataclass, field


class _CalcScanner:
    """
    Finds the characters of FileMaker script text that are syntax.

    Brackets, semicolons and colons are ignored when they are inside:
    - string literals: "..." with backslash escapes (e.g. "a \\" quote")
    - quoted object names: “...” (e.g. layout and script names)
    - calculation comments: /* ... */ and // to the end of the line (but see
      code_chars)

    String literals and /* */ comments may span lines, so the state carries
    over between calls when text is fed one line at a time.
    """

    CODE, STRING, NAME, BLOCK_COMMENT, LINE_COMMENT = range(5)

    def __init__(self):
        self.state = self.CODE

    def code_chars(self, text: str, start: int = 0) -> Iterator[Tuple[int, str]]:
        """
        Yield (index, char) for each syntax character of text from start.

        A // comment ends at a ; or at a ] it doesn't open itself, which are
        yielded: FileMaker writes the rest of the step after a trailing comment
        on the same line, e.g. Set Field By Name [ $f // note ; $id ].
        """
        if self.state == self.LINE_COMMENT:
            self.state = self.CODE  # Each call starts on a new line
        comment_depth = 0
        i = start
        while i < len(text):
            char = text[i]
            next_char = text[i + 1:i + 2]
            if self.state == self.STRING:
                if char == '\\':
                    i += 1  # Skip escaped character
                elif char == '"':
                    self.state = self.CODE
            elif self.state == self.NAME:
                if char == '”':
                    self.state = self.CODE
            elif self.state == self.BLOCK_COMMENT:
                if char == '*' and next_char == '/':
                    self.state = self.CODE
                    i += 1
            elif self.state == self.LINE_COMMENT:
                if char == '\n':
                    self.state = self.CODE
                elif char == '[':
                    comment_depth += 1
                elif char == ']' and comment_depth:
                    comment_depth -= 1
                elif char in (';', ']'):
                    self.state = self.CODE
                    yield i, char
            elif char == '"':
                self.state = self.STRING
            elif char == '“':
                self.state = self.NAME
            elif char == '/' and next_char == '*':
                self.state = self.BLOCK_COMMENT
                i += 1
            elif char == '/' and next_char == '/':
                self.state = self.LINE_COMMENT
                comment_depth = 0
                i += 1
            else:
                yield i, char
            i += 1

    def bracket_balance(self, text: str) -> int:
        """Return the number of syntax '[' minus syntax ']' in text."""
        balance = 0
        for _, char in self.code_chars(text):
            if char == '[':
                balance += 1
            elif char == ']':
                balance -= 1
        return balance


@dataclass
class ParsedStep:
    """
    Represents a parsed FileMaker script step.

    This is the normalized output of the plain-text parser. Each field captures
    a different part of the source line and how it should be treated by the
    generator.

    Example (Set Variable):
        Source line:
            Set Variable [ $var ; Value: 1 ]

        ParsedStep:
            name="Set Variable"
            params={"0": "$var", "Value": "1"}
            raw_text="Set Variable [ $var ; Value: 1 ]"
            line_number=1
            is_comment=False
            comment_text=""
            is_disabled=False

    Fields:
        name:
            Script step name as parsed from the line. Used to select the step
            handler (e.g., "Set Variable", "Go to Layout").

        params:
            Parsed parameters for the step. Positional params are keyed as
            "0", "1", ... while named params use the label (e.g., "Value",
            "With dialog"). Values are preserved as strings for XML generation.

        raw_text:
            The original line text (minus leading/trailing whitespace). Used
            for helper comments and edge-case parsing (e.g., extracting a
            variable name when the param is missing).

        line_number:
            1-based line number in the input. Used for error reporting and
            debugging.

        is_comment:
            True when the line is a comment-only step (e.g., "# note").
            Comment steps are emitted as Comment XML steps.

        comment_text:
            The comment body without the leading "#" marker. Used to populate
            the Comment step Text element.

        is_disabled:
            True when the line is a disabled step (prefixed with "//"). Used
            to set enable="False" on the generated <Step>.
    """

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
            # Normalize HTML entities in sanitized inputs (e.g., &lt;Table Missing&gt;)
            # so parsing doesn't split on entity semicolons.
            import html
            line = html.unescape(line)

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

            # Check for ellipsis truncation marker - if found, preserve it but close brackets
            # This handles files that have been truncated with … marker
            # The ellipsis should be preserved in the calculation as FileMaker exports it that way
            if '…' in line:
                # Find ellipsis position
                ellipsis_pos = line.find('…')
                # Keep everything up to and including the ellipsis
                truncated_line = line[:ellipsis_pos + 1].strip()

                # Try to close brackets if needed (but preserve ellipsis in the content)
                # Count brackets before the ellipsis
                before_ellipsis = line[:ellipsis_pos]
                open_brackets = _CalcScanner().bracket_balance(before_ellipsis)
                if open_brackets > 0:
                    # Add closing brackets after the ellipsis
                    truncated_line += ']' * open_brackets

                line = truncated_line
                # Continue parsing this truncated line as a step

            # Try to parse as a step
            # If it has an opening bracket, collect continuation lines until brackets are balanced
            full_line = line
            if '[' in line:
                # Brackets inside string literals, quoted names and comments don't count
                scanner = _CalcScanner()
                bracket_count = scanner.bracket_balance(line)
                j = i + 1
                while bracket_count > 0 and j < len(lines):
                    # Keep continuation lines verbatim and joined by line breaks:
                    # they can be part of a string literal, and a // comment
                    # ends at the line break
                    next_line = lines[j].rstrip('\r')
                    j += 1
                    # Truncated with ellipsis: keep the text before it and close the step
                    if '…' in next_line:
                        next_line = next_line[:next_line.find('…')].strip()
                        full_line += '\n' + next_line
                        bracket_count += scanner.bracket_balance(next_line)
                        full_line += ']' * max(bracket_count, 0)
                        break

                    full_line += '\n' + next_line
                    bracket_count += scanner.bracket_balance(next_line)
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
        Extract content between matching brackets, handling nested brackets
        and ignoring brackets inside string literals, quoted names and comments.

        Args:
            text: Full text
            start_pos: Position of opening bracket

        Returns:
            Content between brackets (without the brackets themselves)
        """
        if start_pos >= len(text) or text[start_pos] != '[':
            return ""

        depth = 0
        for pos, char in _CalcScanner().code_chars(text, start_pos):
            if char == '[':
                depth += 1
            elif char == ']':
                depth -= 1
                if depth == 0:
                    # Found matching closing bracket
                    return text[start_pos + 1:pos].strip()

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
            # and colons inside quoted strings, names and comments
            colon_pos = -1
            code_chars = _CalcScanner().code_chars(part)
            for i, char in code_chars:
                if char == ':':
                    # Check if it's :: (table reference) or single : (parameter separator)
                    if part[i + 1:i + 2] == ':':
                        # Skip :: (table reference)
                        next(code_chars, None)
                        continue
                    # Found single colon - this is a parameter separator
                    colon_pos = i
                    break

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
        Split text by delimiter, but don't split inside brackets, parentheses,
        quoted strings and names, or comments.

        Args:
            text: Text to split
            delimiter: Delimiter character

        Returns:
            List of parts
        """
        parts = []
        part_start = 0
        bracket_depth = 0
        paren_depth = 0

        for i, char in _CalcScanner().code_chars(text):
            # Handle brackets
            if char == '[':
                bracket_depth += 1
            elif char == ']':
                bracket_depth -= 1
            # Handle parentheses (for function calls)
            elif char == '(':
                paren_depth += 1
            elif char == ')':
                paren_depth -= 1
            elif char == delimiter and bracket_depth == 0 and paren_depth == 0:
                # Found delimiter at top level
                parts.append(text[part_start:i])
                part_start = i + 1

        # Add remaining part
        if part_start < len(text):
            parts.append(text[part_start:])

        return parts

