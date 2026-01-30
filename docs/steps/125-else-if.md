---
id: 125
name: "Else If"
category: Control
status: draft
input_patterns:
  - "Else If [ ... ]"
fm_name: "Else If"
xml:
  step_name: "Else If"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Else If

## Mapping rules

- `name="Else If"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="125"` for all `Else If` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="125" name="Else If">
  
           
  <Calculation>CalcString</Calculation>
  
        
</Step>

```
