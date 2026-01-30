---
id: 70
name: "End If"
category: Control
status: draft
input_patterns:
  - "End If [ ... ]"
fm_name: "End If"
xml:
  step_name: "End If"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: End If

## Mapping rules

- `name="End If"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="70"` for all `End If` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="70" name="End If">
        </Step>

```
