---
id: 124
name: "Set Window Title"
category: Windows
status: draft
input_patterns:
  - "Set Window Title [ ... ]"
fm_name: "Set Window Title"
xml:
  step_name: "Set Window Title"
  enable_default: True
  wrapper: step-only
---

## Description

is present when  is "ByName".

## Mapping rules

- `name="Set Window Title"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="124"` for all `Set Window Title` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="124" name="Set Window Title">
  
          
  <Window value="ByName"/>
  
          
  <Name>
    
            
    <Calculation>
              &quot;Customer Name&quot;
            </Calculation>
    
          
  </Name>
  
          
  <NewName>
    
            
    <Calculation>
              &quot;New Title&quot;
            </Calculation>
    
          
  </NewName>
  
        
</Step>

```
