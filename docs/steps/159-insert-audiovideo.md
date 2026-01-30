---
id: 159
name: "Insert Audio/Video"
category: Fields
status: draft
input_patterns:
  - "Insert Audio/Video [ ... ]"
fm_name: "Insert Audio/Video"
xml:
  step_name: "Insert Audio/Video"
  enable_default: True
  wrapper: step-only
---

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Insert Audio/Video"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="159"` for all `Insert Audio/Video` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="159" name="Insert Audio/Video">
  
            
  <UniversalPathList type="Reference">...</UniversalPathList>
  
        
</Step>

```
