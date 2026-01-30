---
id: 71
name: "Loop"
category: Control
status: draft
input_patterns:
  - "Loop [ ... ]"
fm_name: "Loop"
xml:
  step_name: "Loop"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Loop

## Mapping rules

- `name="Loop"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="71"` for all `Loop` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="71" name="Loop">
        </Step>

```
