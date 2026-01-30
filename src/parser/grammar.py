"""
Lark grammar for FileMaker script syntax.

This grammar defines the structure of plain text FileMaker script steps.
"""

GRAMMAR = r"""
start: script

script: (step | comment)*

// A step consists of a step name and optional parameters in brackets
step: step_name step_params?

// Step name: one or more words, capitalized (e.g., "Set Variable", "Go to Layout")
step_name: WORD (WS+ WORD)*

// Parameters are enclosed in square brackets, separated by semicolons
step_params: "[" param_list? "]"

// Parameter list: one or more parameters separated by semicolons
param_list: param (";" param)*

// A parameter can be:
// - Key-value pair: "Parameter: value"
// - Standalone value: "value"
// - Calculation: any text (handled as value)
param: key_value | value

// Key-value pair: "Key: Value"
key_value: IDENTIFIER ":" value

// Value can be:
// - String literal (quoted)
// - Number
// - Variable ($variable)
// - Calculation (any text, including nested brackets)
// - Identifier (unquoted text)
value: string | number | variable | calculation | identifier

// String literal: "text" or 'text'
string: ESCAPED_STRING

// Number: integer or decimal
number: SIGNED_NUMBER

// Variable: $name
variable: "$" IDENTIFIER

// Calculation: any text that might contain brackets, semicolons, etc.
// We match everything that's not a semicolon or closing bracket
// This is a simplified approach - actual calculations are preserved as-is
calculation: CALC_TEXT

// Identifier: unquoted text (field names, layout names, etc.)
identifier: IDENTIFIER

// Comment: line starting with #
comment: "#" /.*/

// Tokens
WORD: /[A-Z][a-zA-Z0-9]*/
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
ESCAPED_STRING: /"([^"\\]|\\.)*"|'([^'\\]|\\.)*'/
SIGNED_NUMBER: /[+-]?(\d+\.?\d*|\.\d+)/
CALC_TEXT: /[^;\[\]]+/

// Whitespace
WS: /[ \t]+/
%ignore WS

// Newlines are significant (separate steps)
NEWLINE: /\r?\n/
%ignore NEWLINE
"""

