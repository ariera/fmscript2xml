---
id: 56
name: "Insert Picture"
category: Fields
status: draft
input_patterns:
  - "Insert Picture [ ... ]"
fm_name: "Insert Picture"
xml:
  step_name: "Insert Picture"
  enable_default: True
  wrapper: step-only
---

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Insert Picture"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="56"` for all `Insert Picture` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="56" name="Insert Picture">
  
          
  <UniversalPathList type="Reference">...</UniversalPathList>
  
        
</Step>

```
