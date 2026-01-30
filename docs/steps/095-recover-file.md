---
id: 95
name: "Recover File"
category: Files
status: draft
input_patterns:
  - "Recover File [ ... ]"
fm_name: "Recover File"
xml:
  step_name: "Recover File"
  enable_default: True
  wrapper: step-only
---

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Recover File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="95"` for all `Recover File` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="95" name="Recover File">
  
          
  <NoInteract state="True"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
        
</Step>

```
