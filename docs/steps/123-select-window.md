---
id: 123
name: "Select Window"
category: Windows
status: draft
input_patterns:
  - "Select Window [ ... ]"
fm_name: "Select Window"
xml:
  step_name: "Select Window"
  enable_default: True
  wrapper: step-only
---

## Description

is present when  is "ByName".

## Mapping rules

- `name="Select Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="123"` for all `Select Window` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="123" name="Select Window">
  
          
  <Window value="ByName"/>
  
          
  <Name>
    
            
    <Calculation>
              &quot;Customer Name&quot;
            </Calculation>
    
          
  </Name>
  
        
</Step>

```
