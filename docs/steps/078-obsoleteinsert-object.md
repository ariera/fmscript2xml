---
id: 78
name: "#[OBSOLETE]Insert Object"
category: Fields
status: draft
input_patterns:
  - "#[OBSOLETE]Insert Object [ ... ]"
fm_name: "#[OBSOLETE]Insert Object"
xml:
  step_name: "#[OBSOLETE]Insert Object"
  enable_default: True
  wrapper: step-only
---

## Description

is only present if the inserted object is of type "Create

          from File".


Note : Although it makes sense for the 

           attribute to be supported for this script

          step, the setting of the 'Link' checkbox in the Insert Object dialog is

          actually stored in the OLEData element's CDATA, despite the fact that the file

          chosen via this dialog is not (since it is stored in the

           element).
It is no longer possible to create this script; although, you can have step in a converted file.

## Mapping rules

- `name="#[OBSOLETE]Insert Object"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="78"` for all `#[OBSOLETE]Insert Object` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally
  - `{OLE data}` - appears conditionally
  - `{Object Type}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="78" name="#[OBSOLETE]Insert Object">
  
          
  <Set state="True"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
          
  <OLEData>
            ...
          </OLEData>
  
          
  <ObjectType>...</ObjectType>
  
        
</Step>

```
