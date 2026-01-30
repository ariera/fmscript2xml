---
id: 73
name: "End Loop"
category: Control
status: draft
input_patterns:
  - "End Loop [ ... ]"
fm_name: "End Loop"
xml:
  step_name: "End Loop"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: End Loop

## Mapping rules

- `name="End Loop"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="73"` for all `End Loop` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="73" name="End Loop">
        </Step>

```
