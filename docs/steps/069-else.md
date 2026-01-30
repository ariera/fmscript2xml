---
id: 69
name: "Else"
category: Control
status: draft
input_patterns:
  - "Else [ ... ]"
fm_name: "Else"
xml:
  step_name: "Else"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Else

## Mapping rules

- `name="Else"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="69"` for all `Else` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="69" name="Else">
        </Step>

```
