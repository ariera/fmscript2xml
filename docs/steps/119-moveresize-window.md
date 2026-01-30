---
id: 119
name: "Move/Resize Window"
category: Windows
status: draft
input_patterns:
  - "Move/Resize Window [ ... ]"
fm_name: "Move/Resize Window"
xml:
  step_name: "Move/Resize Window"
  enable_default: True
  wrapper: step-only
---

## Description

{See New Window.}

## Mapping rules

- `name="Move/Resize Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="119"` for all `Move/Resize Window` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See New Window for remaining XML}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="119" name="Move/Resize Window">
  
          
  <Window value="Current"/>
  
          ...
        
</Step>

```
