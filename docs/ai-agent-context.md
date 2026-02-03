# AI Agent Context: fmscript2xml

This document is a complete handoff for a new AI agent. It assumes **no prior
knowledge** of this project and captures the architecture, workflows, policies,
and recent fixes/decisions that matter for continued development.

## Purpose

`fmscript2xml` converts **plain text FileMaker script steps** into **FileMaker
XML** (fmxmlsnippet / Script/ObjectList). The output can also be converted to
FileMaker’s clipboard binary format (macOS) so it can be pasted directly into
FileMaker Pro.

The project is deterministic: same input should always yield same output. It is
strict about not inventing database-specific IDs (layout/field/script IDs).

## Quick Orientation

- **Language**: Python
- **Entry point**: `fmscript2xml` CLI (`src/fmscript2xml/converter.py:main`)
- **Parser**: `src/fmscript2xml/parser/parser.py`
- **Step registry**: `src/fmscript2xml/registry/loader.py` loads from
  `src/fmscript2xml/data/steps.json` (pre-compiled from `docs/steps/*.md`)
- **XML generator**: `src/fmscript2xml/generator/step_handlers.py` +
  `src/fmscript2xml/generator/xml_builder.py`
- **Clipboard support (macOS)**: `src/fmscript2xml/fmclip.py`
- **Tests**: `tests/` with DDR-IR validation and real-world fixtures

## Core Principles / Policies

1. **No DB IDs**: Never guess database-specific IDs. For layouts/fields/scripts,
   output `name=...` but omit `id` (see `docs/layout-and-object-ids.md`).
2. **Preserve calculations verbatim**: Calculation text must be preserved
   exactly, typically wrapped in `<![CDATA[ ... ]]>`.
3. **Disabled steps**: Plain text lines starting with `//` are disabled and
   must produce `enable="False"` on the `<Step>` element.
4. **No obsolete steps**: Steps marked as `#[OBSOLETE]` in DDR IR are excluded
   from tests and registry lookup.
5. **Deterministic, explicit mapping**: All step-specific XML comes from handler
   logic or step definitions, never inference from DB.

## CLI

All flags are implemented in `src/fmscript2xml/converter.py`:

- `input` (positional): input text file
- `-o, --output FILE`: output XML path (default `input.txt.xml`)
- `--validate`: validate only
- `--continue-on-error`: continue processing on errors
- `-c, --clipboard`: copy to FileMaker clipboard format (macOS only)
- `--no-file`: skip output file (use with `--clipboard`)
- `--version`: show version and exit
- `-h, --help`: help

Version is maintained in both `src/fmscript2xml/__init__.py` and `setup.py`.

## Step Registry (JSON-based)

`src/fmscript2xml/registry/loader.py` loads step definitions from a pre-compiled
JSON file (`src/fmscript2xml/data/steps.json`).

**Build process**:
- Step definitions are maintained in `docs/steps/*.md` (human-readable documentation)
- Run `python scripts/build_steps_registry.py` to extract minimal metadata
- Generates `src/fmscript2xml/data/steps.json` with only 4 fields per step:
  - `id` — step ID number
  - `name` — step name for matching
  - `xml_step_name` — name in XML `<Step>` element
  - `enable_default` — default enable state

**Performance**: JSON loading is ~10-20x faster than parsing 168 markdown files
with YAML frontmatter. Startup time reduced from ~100-200ms to ~5-10ms.

**Registry API**: Returns simple dicts (not objects) with the 4 fields above.

## Parser (Plain Text → ParsedStep)

`src/fmscript2xml/parser/parser.py`

Key behaviors:

- **Parameter parsing** handles:
  - `::` (table occurrence) vs `:` parameter separators
  - colons inside quoted strings
  - HTML entity unescaping (`&lt;`, `&gt;`)
- **Disabled steps**: detects `//` prefix, sets `ParsedStep.is_disabled`
- **Ellipsis handling**: detects `…` truncation marker, truncates line and
  attempts to close unmatched brackets, while preserving `…` in calculation
- **Nested brackets**: extraction supports nested `[...]`

## XML Generation

`src/fmscript2xml/generator/step_handlers.py` maps step names to handlers.
Handlers create step-specific XML with helper comments as needed.

### Generic XML builder

`src/fmscript2xml/generator/xml_builder.py`:

- `create_step_element()` creates `<Step enable="...">`
- `create_cdata_element()` creates `<Calculation>` (CDATA formatting later)
- `create_field_element()`, `create_layout_element()`, `create_table_element()`
  omit DB IDs by policy
- `create_helper_comment_step()` inserts a `Comment` step that preserves the
  original text when IDs are needed
- `format_xml_with_cdata()` post-processes to create real CDATA sections

### Important Handlers / Fixes

These were added or modified to match FileMaker’s expected XML:

- **Else If**: dedicated handler to output correct XML
- **Open URL** / **Send Mail**: dedicated handlers to produce correct schema
- **Set Error Capture**: outputs `<Set state="True/False"/>`
- **New Window**: outputs `LayoutDestination`, `Name`, dimensions, and
  `NewWndStyles` with correct `Styles` bitmask (Floating Document)
- **Close Window**: outputs `<Window value="Current"/>` and
  `<LimitToWindowsOfCurrentFile state="True"/>`
- **Enter Preview Mode**: outputs `<Pause state="False"/>`
- **Print**: outputs `<NoInteract>` and `<Restore>` only
- **Set Variable**: element order is `Name`, then `Value`, then `Repetition`
- **Set Field By Name**: outputs `<TargetName>` and `<Result>`
- **Commit Records/Requests**: outputs `<NoInteract>`, `<Option>`, and
  `<ESSForceCommit>`
- **Perform Find**: doesn’t add `<Restore>` unless explicitly specified; doesn’t
  add empty `<Query>`
- **Install OnTimer Script**: outputs `<Script>` + `<Interval><Calculation>`
- **Set Field**: handles empty field name (active field), and disabled steps
- **Go to Record/Request/Page**: outputs `<NoInteract>`, `<Exit>`,
  `<RowPageLocation>`, and optional `<Calculation>`
- **Go to Related Record**: outputs `<Option>`, `<MatchAllRecords>`,
  `<ShowInNewWindow>`, `<Restore>`, `<LayoutDestination>`, `<Table>`,
  `<Layout>`, `<Name>`, `<NewWndStyles>`

### Helper Comments

Certain steps require IDs (layout/script/field). The generator inserts a
Comment step with the original text for user guidance.
The semantic comparator removes these helper comments when needed.

## DDR IR (Reference XML)

DDR IR is stored in `docs/DRR XML Grammar/ddr-ir/steps/*.yaml`. It provides
reference XML per step for validation tests.

### Loader

`tests/utils/ddr_ir_loader.py`

- Loads YAML, skips steps with `#[OBSOLETE]`
- Normalizes step names for lookup

### Placeholder Replacement

`tests/utils/fixture_utils.py::_replace_placeholders()`

This function is critical: DDR IR XML is often malformed or includes
placeholders. It:

- Quotes placeholder attribute values
- Removes comment-like placeholders and conditional blocks
- Replaces common placeholders with minimal values
- Removes leftover placeholder attributes
- Fixes malformed XML: duplicate closings, orphaned closing tags, unclosed
  tags, self-closing tags with children, nested `<Step>` blocks, etc.
- Handles unclosed tags (e.g. `DisplayCalculation`, `SMTPEncryptionType`,
  `InputField`, `Sort`, `Restore`, etc.)

## Semantic XML Comparison

`tests/utils/semantic_comparator.py`

Key behavior:

- Extracts steps from both `fmxmlsnippet` and `Script/ObjectList`
- Ignores helper comment steps in some comparisons
- Ignores `hash` attribute for Script/ObjectList steps
- Normalizes comment step names (`# (comment)` to `Comment`)
- Compares `FieldReference`/`TableOccurrenceReference` with `Table::Field`
- Compares calculations with whitespace normalization
- Special handling for `Install OnTimer Script` and `Set Field` empty field names

## Tests

### DDR IR Validation

`tests/test_ddr_ir_validation.py` validates each step handler against DDR IR.
Obsolete steps are not loaded at all (skip removed from tests).

Some steps were previously skipped due to malformed DDR IR, but this was
discouraged by the user (“skipping is not passing”).

### Real-world Fixtures

`tests/test_real_world.py` + `tests/fixtures/real_world/*/input.txt` and
`expected.xml`. These are real FileMaker scripts; **must be gitignored**.

### Simple Fixtures

`tests/test_simples.py` + `tests/fixtures/simple/*/input.txt` and
`expected.xml`. These are small, shareable fixtures.

Fixtures are discovered by:

- `list_fixtures()` for real_world
- `list_simple_fixtures()` for simple

## Gitignore

Real-world fixtures are ignored:

- `.gitignore` includes:
  - `tests/fixtures/real_world/`
  - `tests/fixtures/real_world/**`

This prevents accidental leakage of production scripts.

## Known Problem Areas / Pitfalls

1. **Step name vs. XML element names**:
   - XML element names cannot have spaces. Generic handler sanitizes param keys.
2. **Quoted values**:
   - FileMaker uses curly quotes (`“”`) in some exports; handlers must strip
     both straight and curly quotes when converting names.
3. **`Perform Find` default Restore behavior**:
   - Must not add `<Restore>` unless explicitly specified.
4. **Empty field names**:
   - `Set Field [ ; calculation ]` should omit `<Field>` and treat first param
     as value.
5. **Ellipsis truncation**:
   - Input with `…` should truncate and close brackets; preserve `…`.

## Recent Fixes Worth Preserving

1. Added **Go to Record/Request/Page** and **Go to Related Record** handlers.
2. Added **simple fixture test suite** mirroring real-world tests.
3. Updated README to document all CLI flags.
4. Implemented **clipboard support** via `fmclip.py` and `--clipboard` flag.
5. Fixed **Set Variable** element ordering.
6. Fixed **Open URL** / **Send Mail** XML structure.
7. Fixed **New Window** styles (including Floating Document bitmask).
8. Fixed **Perform Find** defaults.
9. Fixed **disabled steps** handling with `//` prefix.
10. Improved **semantic comparator** for Script/ObjectList XML.

## File Map (Important Files)

- `src/fmscript2xml/__init__.py` — version + exports
- `src/fmscript2xml/converter.py` — CLI
- `src/fmscript2xml/parser/parser.py` — text parser
- `src/fmscript2xml/generator/step_handlers.py` — step-specific XML
- `src/fmscript2xml/generator/xml_builder.py` — XML builders
- `src/fmscript2xml/registry/loader.py` — step definition loader (JSON-based)
- `src/fmscript2xml/data/steps.json` — pre-compiled step registry (runtime)
- `scripts/build_steps_registry.py` — builds JSON from markdown (one-time)
- `docs/steps/*.md` — step definitions and XML snippets (documentation)
- `docs/DRR XML Grammar/ddr-ir/steps/*.yaml` — DDR IR reference XML
- `tests/test_real_world.py` — real-world tests
- `tests/test_simples.py` — simple tests
- `tests/utils/semantic_comparator.py` — semantic diff
- `tests/utils/fixture_utils.py` — fixture utilities

## How to Add a New Step Handler

1. Add logic to `step_handlers.py` with a new class.
2. Register in the `HANDLERS` dict.
3. Ensure mapping matches DDR IR reference XML.
4. If adding a new step definition, edit `docs/steps/*.md` then run:
   - `python scripts/build_steps_registry.py` to regenerate JSON
5. Add/adjust tests in fixtures and run:
   - `pytest tests/test_ddr_ir_validation.py`
   - `pytest tests/test_simples.py`
   - `pytest tests/test_real_world.py` (locally, with ignored fixtures)

## Debug Workflow

1. Run failing tests and inspect semantic diff.
2. Compare expected XML to generated XML.
3. Fix handler or parser; avoid guessing DB IDs.
4. Update DDR IR placeholder handling only if XML is malformed.
5. Re-run tests.

## Additional Notes

- The project uses helper comment steps in cases where FileMaker requires IDs.
  These comments are acceptable and filtered in comparisons as needed.
- Keep XML element ordering aligned with FileMaker exports.
- Use `docs/system-prompt.md` and `docs/layout-and-object-ids.md` for policy.
