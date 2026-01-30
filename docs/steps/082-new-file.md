---
id: 82
name: "New File"
category: Files
status: draft
input_patterns:
  - "New File [ ... ]"
fm_name: "New File"
xml:
  step_name: "New File"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: New File

## Mapping rules

- `name="New File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="82"` for all `New File` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="82" name="New File">
        </Step>

```
