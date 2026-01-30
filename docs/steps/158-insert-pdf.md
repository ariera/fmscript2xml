---
id: 158
name: "Insert PDF"
category: Fields
status: draft
input_patterns:
  - "Insert PDF [ ... ]"
fm_name: "Insert PDF"
xml:
  step_name: "Insert PDF"
  enable_default: True
  wrapper: step-only
---

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Insert PDF"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="158"` for all `Insert PDF` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="158" name="Insert PDF">
  
            
  <UniversalPathList type="Reference">...</UniversalPathList>
  
        
</Step>

```
