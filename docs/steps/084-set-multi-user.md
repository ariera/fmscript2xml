---
id: 84
name: "Set Multi-User"
category: Files
status: draft
input_patterns:
  - "Set Multi-User [ ... ]"
fm_name: "Set Multi-User"
xml:
  step_name: "Set Multi-User"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Multi-User

## Mapping rules

- `name="Set Multi-User"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="84"` for all `Set Multi-User` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="84" name="Set Multi-User">
  
          
  <MultiUser value="True"/>
  
        
</Step>

```
