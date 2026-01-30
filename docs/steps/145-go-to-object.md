---
id: 145
name: "Go to Object"
category: Control
status: draft
input_patterns:
  - "Go to Object [ ... ]"
fm_name: "Go to Object"
xml:
  step_name: "Go to Object"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Go to Object

## Mapping rules

- `name="Go to Object"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="145"` for all `Go to Object` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="145" name="Go to Object">
  
           
  <ObjectName>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </ObjectName>
  
           
  <Repetition>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
