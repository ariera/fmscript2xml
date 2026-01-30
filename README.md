# FileMaker Script to XML Parser

A robust, deterministic parser/compiler for converting plain text FileMaker script snippets into valid XML format.

## Overview

This project provides a rule-based parser that converts human-readable FileMaker script steps (written in plain text) into the XML format used by FileMaker's Database Design Report (DDR) and script import/export functionality.

This parser uses deterministic parsing rules and loads step definitions from the documentation included in this repository.

## Features

- **Deterministic**: Same input always produces same output
- **Fast**: No API calls, pure Python parsing
- **Reliable**: Explicit error handling and validation
- **Complete**: Supports all 167 documented FileMaker script steps
- **Safe**: Never guesses database-specific IDs, follows strict policies

## Installation

```bash
pip install -e .
```

## Usage

### Basic Usage

```python
from fmscript2xml import Converter

converter = Converter()
xml_output = converter.convert("""
Set Variable [ $LastError ; Value: 0 ]
If [ Get ( FoundCount ) = 0 ]
    Exit Script [ Text Result: $ScriptResult ]
End If
""")

print(xml_output)
```

### Command Line

```bash
# Convert script to XML (creates input.txt.xml next to input file)
fmscript2xml input.txt

# Specify custom output file
fmscript2xml input.txt -o output.xml

# Validate only (no conversion)
fmscript2xml input.txt --validate

# Continue processing on errors
fmscript2xml input.txt --continue-on-error
```

### Advanced Usage

```python
from fmscript2xml import Converter

converter = Converter()

# Validate script
is_valid, errors = converter.validate(script_text)
if not is_valid:
    for error in errors:
        print(f"Error: {error}")

# Convert with error handling
try:
    xml = converter.convert(script_text, stop_on_error=True)
except UnknownStepError as e:
    print(f"Unknown step: {e.step_name}")
```

## Examples

See `examples/example_usage.py` for more detailed examples.

## Project Structure

- `src/parser/`: Lexer and parser for plain text script syntax
- `src/registry/`: Step definition loader from documentation
- `src/generator/`: XML generation from parsed steps
- `tests/`: Comprehensive test suite
- `docs/`: Documentation and step definitions
  - `steps/`: Individual step definition markdown files (167 steps)
  - `layout-and-object-ids.md`: Policy for handling database-specific IDs
  - `DRR XML Grammar/`: Reference documentation for FileMaker XML format
  - `system-prompt.md` and `steps-documentation.md`: AI agent documentation (for reference)

## Documentation

This parser loads step definitions from `docs/steps/` at runtime. It follows strict policies:
- **Database ID omission**: Never guesses database-specific IDs (see `docs/layout-and-object-ids.md`)
- **Calculation preservation**: All calculations preserved exactly as written
- **Helper comment generation**: Adds comments for manual developer intervention when needed

See `docs/README.md` for more information about the documentation structure.

## License

See parent project license.

