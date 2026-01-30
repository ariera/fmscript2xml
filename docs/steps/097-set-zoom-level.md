---
id: 97
name: "Set Zoom Level"
category: Windows
status: draft
input_patterns:
  - "Set Zoom Level [ ... ]"
fm_name: "Set Zoom Level"
xml:
  step_name: "Set Zoom Level"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Zoom Level

## Mapping rules

- `name="Set Zoom Level"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="97"` for all `Set Zoom Level` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="97" name="Set Zoom Level">
  
          
  <Lock state="True"/>
  
          
  <Zoom value="75"/>
  
        
</Step>

```
