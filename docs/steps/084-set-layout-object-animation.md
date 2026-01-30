---
id: 84
name: "Set Layout Object Animation"
category: Control
status: draft
input_patterns:
  - "Set Layout Object Animation [ ... ]"
fm_name: "Set Layout Object Animation"
xml:
  step_name: "Set Layout Object Animation"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Layout Object Animation

## Mapping rules

- `name="Set Layout Object Animation"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="84"` for all `Set Layout Object Animation` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="true" id="84" name="Set Layout Object Animation">
           <Set state="true"|"false"/>
        </Step>
```
