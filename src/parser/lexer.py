"""
Lexer for FileMaker script syntax.

Handles tokenization of input text, preserving calculation whitespace
and handling multi-line steps.
"""

import re
from typing import List, Tuple, Optional


class Token:
    """Represents a token in the input stream."""

    def __init__(self, type: str, value: str, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {self.value!r}, line={self.line}, col={self.column})"


class Lexer:
    """
    Tokenizes FileMaker script text.

    Handles:
    - Step boundaries (newlines)
    - Comments (lines starting with #)
    - Multi-line steps (continuation)
    - Preserving whitespace in calculations
    """

    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []

    def tokenize(self) -> List[Token]:
        """Tokenize the input text and return list of tokens."""
        while self.pos < len(self.text):
            # Skip whitespace (but track newlines for line numbers)
            if self.text[self.pos] == '\n':
                self.line += 1
                self.column = 1
                self.pos += 1
                continue
            elif self.text[self.pos].isspace():
                self.column += 1
                self.pos += 1
                continue

            # Comments (lines starting with #)
            if self.text[self.pos] == '#' and (self.pos == 0 or self.text[self.pos - 1] == '\n'):
                token = self._read_comment()
                if token:
                    self.tokens.append(token)
                continue

            # Brackets
            if self.text[self.pos] == '[':
                self.tokens.append(Token('LBRACKET', '[', self.line, self.column))
                self.pos += 1
                self.column += 1
                continue
            elif self.text[self.pos] == ']':
                self.tokens.append(Token('RBRACKET', ']', self.line, self.column))
                self.pos += 1
                self.column += 1
                continue

            # Semicolon (parameter separator)
            if self.text[self.pos] == ';':
                self.tokens.append(Token('SEMICOLON', ';', self.line, self.column))
                self.pos += 1
                self.column += 1
                continue

            # Colon (key-value separator)
            if self.text[self.pos] == ':':
                self.tokens.append(Token('COLON', ':', self.line, self.column))
                self.pos += 1
                self.column += 1
                continue

            # String literals
            if self.text[self.pos] in ('"', "'"):
                token = self._read_string()
                if token:
                    self.tokens.append(token)
                continue

            # Variables ($name)
            if self.text[self.pos] == '$':
                token = self._read_variable()
                if token:
                    self.tokens.append(token)
                continue

            # Numbers
            if self.text[self.pos].isdigit() or (self.text[self.pos] in '+-' and
                                                  self.pos + 1 < len(self.text) and
                                                  self.text[self.pos + 1].isdigit()):
                token = self._read_number()
                if token:
                    self.tokens.append(token)
                continue

            # Identifiers and words
            token = self._read_identifier_or_word()
            if token:
                self.tokens.append(token)
                continue

            # Unknown character - skip with warning
            self.pos += 1
            self.column += 1

        return self.tokens

    def _read_comment(self) -> Optional[Token]:
        """Read a comment line."""
        start_pos = self.pos
        start_col = self.column

        # Read until newline
        while self.pos < len(self.text) and self.text[self.pos] != '\n':
            self.pos += 1
            self.column += 1

        value = self.text[start_pos:self.pos]
        return Token('COMMENT', value, self.line, start_col)

    def _read_string(self) -> Optional[Token]:
        """Read a string literal."""
        quote_char = self.text[self.pos]
        start_pos = self.pos
        start_col = self.column

        self.pos += 1  # Skip opening quote
        self.column += 1

        # Read until closing quote (handle escaped quotes)
        while self.pos < len(self.text):
            if self.text[self.pos] == '\\' and self.pos + 1 < len(self.text):
                # Escaped character
                self.pos += 2
                self.column += 2
            elif self.text[self.pos] == quote_char:
                # Closing quote
                self.pos += 1
                self.column += 1
                break
            else:
                self.pos += 1
                self.column += 1

        value = self.text[start_pos:self.pos]
        return Token('STRING', value, self.line, start_col)

    def _read_variable(self) -> Optional[Token]:
        """Read a variable ($name)."""
        start_pos = self.pos
        start_col = self.column

        self.pos += 1  # Skip $
        self.column += 1

        # Read identifier
        while self.pos < len(self.text) and (self.text[self.pos].isalnum() or
                                             self.text[self.pos] == '_'):
            self.pos += 1
            self.column += 1

        value = self.text[start_pos:self.pos]
        return Token('VARIABLE', value, self.line, start_col)

    def _read_number(self) -> Optional[Token]:
        """Read a number."""
        start_pos = self.pos
        start_col = self.column

        # Optional sign
        if self.text[self.pos] in '+-':
            self.pos += 1
            self.column += 1

        # Integer part
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            self.pos += 1
            self.column += 1

        # Decimal point and fractional part
        if self.pos < len(self.text) and self.text[self.pos] == '.':
            self.pos += 1
            self.column += 1
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                self.pos += 1
                self.column += 1

        value = self.text[start_pos:self.pos]
        return Token('NUMBER', value, self.line, start_col)

    def _read_identifier_or_word(self) -> Optional[Token]:
        """Read an identifier or word."""
        start_pos = self.pos
        start_col = self.column

        # Read alphanumeric and underscore
        while self.pos < len(self.text) and (self.text[self.pos].isalnum() or
                                            self.text[self.pos] in '_ '):
            self.pos += 1
            self.column += 1

        if self.pos == start_pos:
            return None

        value = self.text[start_pos:self.pos].strip()
        if not value:
            return None

        # Determine if it's a word (capitalized) or identifier
        if value[0].isupper() and ' ' in value:
            return Token('WORD', value, self.line, start_col)
        else:
            return Token('IDENTIFIER', value, self.line, start_col)

