---
id: 152
name: "Save Records as Snapshot Link"
category: Records
status: draft
input_patterns:
  - "Save Records as Snapshot Link [ ... ]"
fm_name: "Save Records as Snapshot Link"
xml:
  step_name: "Save Records as Snapshot Link"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Save Records as Snapshot Link

## Mapping rules

- `name="Save Records as Snapshot Link"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="152"` for all `Save Records as Snapshot Link` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="152" name="Save Records as Snapshot Link">
  
             
  <CreateEmail state="True"/>
  
             
  <CreateDirectories state="True"/>
  
             
  <UniversalPathList>...</UniversalPathList>
  
             
  <SaveType value="BrowsedRecords"/>
  
         
</Step>

```
