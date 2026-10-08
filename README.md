> [!CAUTION]
> **This project is discontinued.** The Python package and CLI are no longer
> maintained. They are replaced by **[fmscript2xml for macOS](https://github.com/ariera/fmscript2xml-app)**, a
> native menu bar app.

<p align="center">
  <a href="https://github.com/ariera/fmscript2xml-app"><img src="https://raw.githubusercontent.com/ariera/fmscript2xml-app/main/docs/logo.png" width="96" alt="fmscript2xml logo"></a>
</p>

<h2 align="center"><a href="https://github.com/ariera/fmscript2xml-app">➡️ Use the new fmscript2xml app</a></h2>

<p align="center">
  Copy FileMaker script steps as text, press <b>⌃⌥⌘F</b>, paste them into the Script Workspace as real steps.<br>
  No Python, no Automator, and FileMaker doesn't need to be installed for the conversion.
</p>

<p align="center">
  <a href="https://github.com/ariera/fmscript2xml-app/releases/latest"><b>Download the latest release</b></a> ·
  <a href="https://github.com/ariera/fmscript2xml-app#readme">Documentation</a>
</p>

<p align="center">
  <a href="https://github.com/ariera/fmscript2xml-app"><img src="https://raw.githubusercontent.com/ariera/fmscript2xml-app/main/docs/images/workflow.gif" width="640" alt="Copy script steps as text, press ⌃⌥⌘F, paste them into FileMaker as steps"></a>
</p>

### Moving to the app

| You used… | Now |
|---|---|
| The Automator Quick Action with ⌃⌥⌘F | Install the app, then turn the old shortcut off in System Settings → Keyboard → Keyboard Shortcuts → Services so the two don't collide. |
| `fmscript2xml --from-clipboard --clipboard --no-file` | Press ⌃⌥⌘F. The app also keeps a history of conversions and has an inspector for errors. |
| The `fmscript2xml` CLI on files | The app repo includes a Swift CLI with the same options: `swift run fmscript2xml script.txt`. |
| `from fmscript2xml import Converter` | No replacement library. This package keeps working at v0.5.4 but won't get fixes. |

Bug reports and feature requests go to the [new repository](https://github.com/ariera/fmscript2xml-app/issues).

---

<details>
<summary><b>Legacy documentation (v0.5.4, unmaintained)</b></summary>

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

### Install from GitHub

```bash
pip install git+https://github.com/ariera/fmscript2xml.git
```

### Install from Local Copy

If you have cloned the repository locally:

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

The `fmscript2xml` command-line tool provides a simple interface for converting FileMaker scripts to XML.

#### Basic Usage

```bash
# Convert script to XML (creates input.txt.xml next to input file)
fmscript2xml input.txt

# Specify custom output file
fmscript2xml input.txt -o output.xml
```

#### Command-Line Options

| Flag | Description |
|------|-------------|
| `input` | Input file containing plain text FileMaker script (required) |
| `-o, --output FILE` | Output file path for XML. If not specified, creates `input.xml` next to the input file |
| `--validate` | Only validate the script, do not convert to XML |
| `--continue-on-error` | Continue processing even when errors are encountered |
| `--from-clipboard` | Read input script from clipboard (macOS only). Requires `--output` or `--no-file` |
| `-c, --clipboard` | Copy result to clipboard as FileMaker objects (macOS only). The XML is converted to FileMaker's binary clipboard format and can be pasted directly into FileMaker Pro |
| `--no-file` | Do not write output file. Useful when combined with `--clipboard` to only copy to clipboard |
| `--version` | Show program version and exit |
| `-h, --help` | Show help message and exit |

#### Examples

```bash
# Basic conversion
fmscript2xml script.txt

# Convert to specific output file
fmscript2xml script.txt -o output.xml

# Validate script without converting
fmscript2xml script.txt --validate

# Convert and copy to clipboard (macOS only)
fmscript2xml script.txt --clipboard

# Copy to clipboard without creating a file
fmscript2xml script.txt --clipboard --no-file

# Convert from clipboard text to a file (macOS only)
fmscript2xml --from-clipboard --output clipboard.xml

# Clipboard in, FileMaker objects out (macOS only)
fmscript2xml --from-clipboard --no-file --clipboard

# Continue processing even if errors occur
fmscript2xml script.txt --continue-on-error

# Show version
fmscript2xml --version
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

- **[macOS: Global keyboard shortcut](docs/automator-keyboard-shortcut.md)** — Set up a hotkey that converts clipboard text to FileMaker’s binary format so you can paste directly into the Script editor. Great for copying script snippets (e.g. from docs or AI-generated code) and pasting them into FileMaker without manual conversion, speeding up development.

This parser loads step definitions from `docs/steps/` at runtime. It follows strict policies:
- **Database ID omission**: Never guesses database-specific IDs (see `docs/layout-and-object-ids.md`)
- **Calculation preservation**: All calculations preserved exactly as written
- **Helper comment generation**: Adds comments for manual developer intervention when needed

See `docs/README.md` for more information about the documentation structure.

## License

See parent project license.


</details>
