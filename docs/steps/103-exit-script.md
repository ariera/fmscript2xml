---
id: 103
name: "Exit Script"
category: Control
status: draft
input_patterns:
  - "Exit Script [ ... ]"
fm_name: "Exit Script"
xml:
  step_name: "Exit Script"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Exit Script

## Mapping rules

- `name="Exit Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="103"` for all `Exit Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="103" name="Exit Script">
  
            
  <Calculation>
               CalcString
            </Calculation>
  
        
</Step>

```
