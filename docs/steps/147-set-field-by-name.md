---
id: 147
name: "Set Field By Name"
category: Fields
status: draft
input_patterns:
  - "Set Field By Name [ ... ]"
fm_name: "Set Field By Name"
xml:
  step_name: "Set Field By Name"
  enable_default: True
  wrapper: step-only
---

## Description

specifies the target field's name
 specifies the value to be placed in that field.

## Mapping rules

- `name="Set Field By Name"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="147"` for all `Set Field By Name` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="147" name="Set Field By Name">
  

  <TargetName>
    
          
    <Calculation>
          CalcString
          </Calculation>
    
          
  </TargetName>
  
 
  <Result>
    
             
    <Calculation>
                  CalcString
             </Calculation>
    
          
  </Result>
  

</Step>

```
