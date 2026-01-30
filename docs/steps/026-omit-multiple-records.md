---
id: 26
name: "Omit Multiple Records"
category: Found Sets
status: draft
input_patterns:
  - "Omit Multiple Records [ ... ]"
fm_name: "Omit Multiple Records"
xml:
  step_name: "Omit Multiple Records"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Omit Multiple Records

## Mapping rules

- `name="Omit Multiple Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="26"` for all `Omit Multiple Records` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="26" name="Omit Multiple Records">
  
          
  <NoInteract state="True"/>
  
            
  <Calculation>
              CalcString
            </Calculation>
  
        
</Step>

```
