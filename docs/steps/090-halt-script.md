---
id: 90
name: "Halt Script"
category: Control
status: draft
input_patterns:
  - "Halt Script [ ... ]"
fm_name: "Halt Script"
xml:
  step_name: "Halt Script"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Halt Script

## Mapping rules

- `name="Halt Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="90"` for all `Halt Script` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="90" name="Halt Script">
        </Step>

```
