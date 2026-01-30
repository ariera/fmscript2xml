---
id: 167
name: "Refresh Object"
category: Miscellaneous
status: draft
input_patterns:
  - "Refresh Object [ ... ]"
fm_name: "Refresh Object"
xml:
  step_name: "Refresh Object"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Refresh Object

## Mapping rules

- `name="Refresh Object"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="167"` for all `Refresh Object` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="167" name="Refresh Object">
  
           
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
