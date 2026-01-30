---
id: 180
name: "Refresh Portal"
category: Miscellaneous
status: draft
input_patterns:
  - "Refresh Portal [ ... ]"
fm_name: "Refresh Portal"
xml:
  step_name: "Refresh Portal"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Refresh Portal

## Mapping rules

- `name="Refresh Portal"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="180"` for all `Refresh Portal` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="180" name="Refresh Portal">
  
           
  <ObjectName>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </ObjectName>
  
        
</Step>

```
