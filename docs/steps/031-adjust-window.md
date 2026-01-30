---
id: 31
name: "Adjust Window"
category: Windows
status: draft
input_patterns:
  - "Adjust Window [ ... ]"
fm_name: "Adjust Window"
xml:
  step_name: "Adjust Window"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Adjust Window

## Mapping rules

- `name="Adjust Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="31"` for all `Adjust Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="31" name="Adjust Window">
  
          
  <WindowState value="Maximize"/>
  
        
</Step>

```
