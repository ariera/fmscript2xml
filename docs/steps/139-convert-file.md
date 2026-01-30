---
id: 139
name: "Convert File"
category: Files
status: draft
input_patterns:
  - "Convert File [ ... ]"
fm_name: "Convert File"
xml:
  step_name: "Convert File"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Convert File

## Mapping rules

- `name="Convert File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="139"` for all `Convert File` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Import Records, except for folder data source options,
           which Convert File does not have.}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="139" name="Convert File">
          ...
        </Step>

```
