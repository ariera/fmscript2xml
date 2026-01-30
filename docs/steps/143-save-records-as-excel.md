---
id: 143
name: "Save Records as Excel"
category: Records
status: draft
input_patterns:
  - "Save Records as Excel [ ... ]"
fm_name: "Save Records as Excel"
xml:
  step_name: "Save Records as Excel"
  enable_default: True
  wrapper: step-only
---

## Description

may not be generated if there is no output file specified in the script step.
 value of "XLXE" means export to "Excel workbook (.xlsx)" type.

## Mapping rules

- `name="Save Records as Excel"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="143"` for all `Save Records as Excel` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="143" name="Save Records as Excel">
  
            
  <NoInteract state="True"/>
  
            
  <Restore state="True"/>
  
            
  <AutoOpen state="True"/>
  
            
  <CreateEmail state="True"/>
  
            
  <CreateDirectories state="True"/>
  
            
  <UniversalPathList>...</UniversalPathList>
  
            
  <SaveType value="BrowsedRecords"/>
  
            
  <UseFieldNames state="True"/>
  
            
  <WorkSheet>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </WorkSheet>
  
            
  <Title>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </Title>
  
            
  <Subject>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </Subject>
  
            
  <Author>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </Author>
  
        
</Step>

```
