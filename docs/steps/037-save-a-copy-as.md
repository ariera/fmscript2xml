---
id: 37
name: "Save a Copy as"
category: Files
status: draft
input_patterns:
  - "Save a Copy as [ ... ]"
fm_name: "Save a Copy as"
xml:
  step_name: "Save a Copy as"
  enable_default: True
  wrapper: step-only
---

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Save a Copy as"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="37"` for all `Save a Copy as` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="37" name="Save a Copy as">
  
          
  <AutoOpen state="True"/>
  
          
  <CreateEmail state="True"/>
  
          
  <CreateDirectories state="True"/>
  
          
  <SaveAsType value="Copy"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
        
</Step>

```
