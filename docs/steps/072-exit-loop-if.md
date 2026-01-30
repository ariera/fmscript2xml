---
id: 72
name: "Exit Loop If"
category: Control
status: draft
input_patterns:
  - "Exit Loop If [ ... ]"
fm_name: "Exit Loop If"
xml:
  step_name: "Exit Loop If"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Exit Loop If

## Mapping rules

- `name="Exit Loop If"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="72"` for all `Exit Loop If` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="72" name="Exit Loop If">
  
           
  <Calculation>
              CalcString
           </Calculation>
  
        
</Step>

```
