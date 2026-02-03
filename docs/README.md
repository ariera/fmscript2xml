# Documentation

This directory contains the documentation and step definitions used by the `fmscript2xml` parser.

## Contents

### `steps/`

Contains individual markdown files for each FileMaker script step (167 total). Each file includes:

- YAML frontmatter with step metadata (id, name, category, status)
- Description of the step
- Input patterns (plain text format)
- Mapping rules (how to convert to XML)
- XML examples showing the expected output format
- Conditional elements (XML elements that only appear under certain conditions)

**File naming**: Files are named with the step ID (zero-padded to 3 digits) and step name, e.g., `001-perform-script.md`, `141-set-variable.md`.

**Runtime usage**: These markdown files are NOT loaded at runtime. Instead, they are pre-compiled into a compact JSON file (`src/fmscript2xml/data/steps.json`) that is bundled with the package. The JSON file contains only the minimal metadata needed for conversion (id, name, xml_step_name, enable_default).

### `layout-and-object-ids.md`

Critical policy document explaining how to handle database-specific IDs. This is a core safety feature:

- **Never guess or fabricate** database-specific IDs (layout IDs, table IDs, field IDs)
- **Omit the `id` attribute** and use only `name` (or calculation)
- **Add helper comment steps** before steps that reference named objects, containing the original plain text

This ensures the generated XML is safe, valid, and can be manually corrected by developers.

### `DRR XML Grammar/`

Reference documentation for the FileMaker XML format:

- `readme.md`: Overview of the DDR XML Grammar
- `steps-documentation-for-ddr.html`: Official FileMaker documentation extracted from the Database Design Report

This is provided for reference when understanding the XML structure or adding new step definitions.

### `system-prompt.md` and `steps-documentation.md`

These files are included for reference and were originally created for AI agent systems. They contain:

- `system-prompt.md`: Concise instructions for converting plain text to XML
- `steps-documentation.md`: Complete documentation of all script steps in a single file

While the `fmscript2xml` parser doesn't use these files directly, they may be useful for:
- Understanding the conversion process
- Reference when adding new step definitions
- Integration with AI-based systems

## Source

This documentation was originally developed in the `MyGPT-txt2xml` project and has been extracted here to make `fmscript2xml` a standalone, publishable project.

The step definitions were generated from the official FileMaker DDR (Database Design Report) HTML documentation using automated parsing scripts.

## Updating Documentation

To add or update step definitions:

1. Edit the appropriate file in `steps/` (or create a new one following the naming convention)
2. Follow the existing format with YAML frontmatter and markdown sections
3. Include real examples from actual FileMaker XML exports
4. Ensure the mapping rules are clear and complete
5. **Regenerate the JSON registry**: Run `python scripts/build_steps_registry.py` to rebuild `src/fmscript2xml/data/steps.json`
6. Test that the parser can load and use the updated definition

For questions about the XML format, refer to `DRR XML Grammar/` or the official FileMaker documentation.

### Regenerating the Step Registry

After editing any step definition in `steps/`, you must regenerate the JSON registry:

```bash
python scripts/build_steps_registry.py
```

This script:
- Reads all markdown files from `docs/steps/*.md`
- Extracts only the minimal metadata needed at runtime (id, name, xml_step_name, enable_default)
- Writes to `src/fmscript2xml/data/steps.json`

The JSON file is what gets bundled with the package and loaded at runtime for fast startup (~10-20x faster than parsing markdown files).
