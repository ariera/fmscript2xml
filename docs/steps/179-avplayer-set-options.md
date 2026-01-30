---
id: 179
name: "AVPlayer Set Options"
category: Miscellaneous
status: draft
input_patterns:
  - "AVPlayer Set Options [ ... ]"
fm_name: "AVPlayer Set Options"
xml:
  step_name: "AVPlayer Set Options"
  enable_default: True
  wrapper: step-only
---

## Description

All parameters are optional. This step is used to adjust the settings of a player that is either playing or paused. The parameters that are the same as in AVPlayer Play have the same meaning as in that step.

## Mapping rules

- `name="AVPlayer Set Options"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="179"` for all `AVPlayer Set Options` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Script step text}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="179" name="AVPlayer Set Options">
  
           value=&quot;Start Full Screen&quot;
          
  <HideControls value="True"/>
  
          
  <DisableExternalControls value="True"/>
  
          
  <DisableInteraction value="True"/>
  
            
  <Calculation>30</Calculation>
  
          
  <StartOffset>
    
            
    <Calculation>20</Calculation>
    
          
  </StartOffset>
  
          
  <EndOffset>
    
            
    <Calculation>120</Calculation>
    
          
  </EndOffset>
  
          
  <Volume>
    
            
    <Calculation>.5</Calculation>
    
          
  </Volume>
  
          
  <Zoom value="Fit"/>
  
          
  <Sequence value="Previous"/>
  
        
</Step>

```
