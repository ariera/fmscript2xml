---
id: 86
name: "Set Error Capture"
category: Control
status: draft
input_patterns:
  - "Set Error Capture [ ... ]"
fm_name: "Set Error Capture"
xml:
  step_name: "Set Error Capture"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Error Capture

## Mapping rules

- `name="Set Error Capture"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="86"` for all `Set Error Capture` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="86" name="Set Error Capture">
  
           
  <Set state="True"/>
  
        
</Step>

```
