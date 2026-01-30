---
id: 25
name: "Omit Record"
category: Found Sets
status: draft
input_patterns:
  - "Omit Record [ ... ]"
fm_name: "Omit Record"
xml:
  step_name: "Omit Record"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Omit Record

## Mapping rules

- `name="Omit Record"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="25"` for all `Omit Record` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="25" name="Omit Record">
        </Step>

```
