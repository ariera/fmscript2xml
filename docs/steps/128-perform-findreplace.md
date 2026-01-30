---
id: 128
name: "Perform Find/Replace"
category: Editing
status: draft
input_patterns:
  - "Perform Find/Replace [ ... ]"
fm_name: "Perform Find/Replace"
xml:
  step_name: "Perform Find/Replace"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Perform Find/Replace

## Mapping rules

- `name="Perform Find/Replace"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="128"` for all `Perform Find/Replace` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="128" name="Perform Find/Replace">
  
          
  <NoInteract state="True"/>
  
          
  <FindReplaceOperation type="FindNext" direction="Forward" MatchCase="False" MatchWholeWords="False" AcrossOptions="All" WithinOptions="All"/>
  
          
  <FindCalc>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </FindCalc>
  
          
  <ReplaceCalc>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </ReplaceCalc>
  
        
</Step>

```
