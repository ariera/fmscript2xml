---
id: 122
name: "New Window"
category: Windows
status: draft
input_patterns:
  - "New Window [ ... ]"
fm_name: "New Window"
xml:
  step_name: "New Window"
  enable_default: True
  wrapper: step-only
---

## Description

element is output only
          if  is not "OriginalLayout."
  element is output only if  is "LayoutNameByCalc" or "LayoutNumberByCalc."
  is required in case there is more than one layout with the same name.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="New Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="122"` for all `New Window` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Layout id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Layout>` element specifies the target layout.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{value}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="122" name="New Window">
  
          
  <Name>
    
            
    <Calculation>
              &quot;WindowName&quot;
            </Calculation>
    
          
  </Name>
  
          
  <Height>
    
            
    <Calculation>
              200
            </Calculation>
    
          
  </Height>
  
          
  <Width>
    
            
    <Calculation>
              400
            </Calculation>
    
          
  </Width>
  
          
  <DistanceFromTop>
    
            
    <Calculation>
              100
            </Calculation>
    
          
  </DistanceFromTop>
  
          
  <DistanceFromLeft>
    
            
    <Calculation>
              125
            </Calculation>
    
          
  </DistanceFromLeft>
  
   
  <NewWndStyles Style="Dialog" Close="Yes" Minimize="No" Maximize="Yes" Resize="Yes" MenuBar="Yes" DimParentWindow="No" Styles="..."/>
  
  
  <LayoutDestination value="SelectedLayout"/>
  
            
  <Layout name="LayoutName" id="1"/>
  
        
</Step>

```
