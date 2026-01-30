---
id: 121
name: "Close Window"
category: Windows
status: draft
input_patterns:
  - "Close Window [ ... ]"
fm_name: "Close Window"
xml:
  step_name: "Close Window"
  enable_default: True
  wrapper: step-only
---

## Description

is present when  is "ByName".

## Mapping rules

- `name="Close Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="121"` for all `Close Window` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="121" name="Close Window">
  
          
  <Window value="ByName"/>
  
          
  <Name>
    
            
    <Calculation>
              &quot;Customer Name&quot;
            </Calculation>
    
          
  </Name>
  
        
</Step>

```
