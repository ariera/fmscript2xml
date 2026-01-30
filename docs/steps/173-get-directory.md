---
id: 173
name: "Get Directory"
category: Miscellaneous
status: draft
input_patterns:
  - "Get Directory [ ... ]"
fm_name: "Get Directory"
xml:
  step_name: "Get Directory"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Get Directory

## Mapping rules

- `name="Get Directory"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="173"` for all `Get Directory` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Variable name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="173" name="Get Directory">
  
             
  <AllowFolderCreation state="True"/>
  

  <Name>...</Name>
  

  <DialogTitle>
    
            
    <Calculation>
          CalcString
          </Calculation>
    
          
  </DialogTitle>
  

  <DefaultLocation>
    
          
    <Calculation>
          CalcString
          </Calculation>
    
          
  </DefaultLocation>
  
         
</Step>

```
