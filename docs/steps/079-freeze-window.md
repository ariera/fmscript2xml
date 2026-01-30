---
id: 79
name: "Freeze Window"
category: Windows
status: draft
input_patterns:
  - "Freeze Window [ ... ]"
fm_name: "Freeze Window"
xml:
  step_name: "Freeze Window"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Freeze Window

## Mapping rules

- `name="Freeze Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="79"` for all `Freeze Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="79" name="Freeze Window">
        </Step>

```
