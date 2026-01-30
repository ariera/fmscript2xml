---
id: 141
name: "Set Variable"
category: Control
status: draft
input_patterns:
  - "Set Variable [ ... ]"
fm_name: "Set Variable"
xml:
  step_name: "Set Variable"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Variable

## Mapping rules

- `name="Set Variable"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="141"` for all `Set Variable` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Variable name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="141" name="Set Variable">
  
            
  <Name>...</Name>
  
            
  <Value>
    
               
    <Calculation>
                CalcString
               </Calculation>
    
            
  </Value>
  
            
  <Repetition>
    
               
    <Calculation>
                CalcString
               </Calculation>
    
            
  </Repetition>
  
        
</Step>

```
