---
id: 146
name: "Set Web Viewer"
category: Control
status: draft
input_patterns:
  - "Set Web Viewer [ ... ]"
fm_name: "Set Web Viewer"
xml:
  step_name: "Set Web Viewer"
  enable_default: True
  wrapper: step-only
---

## Description

element is present when 

         is "GoToURL."

## Mapping rules

- `name="Set Web Viewer"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="146"` for all `Set Web Viewer` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="146" name="Set Web Viewer">
  
           
  <Action value="Reset"/>
  
           
  <ObjectName>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </ObjectName>
  
           
  <URL custom="True">
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </URL>
  
        
</Step>

```
