---
id: 166
name: "Show/Hide Menubar"
category: Windows
status: draft
input_patterns:
  - "Show/Hide Menubar [ ... ]"
fm_name: "Show/Hide Menubar"
xml:
  step_name: "Show/Hide Menubar"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Show/Hide Menubar

## Mapping rules

- `name="Show/Hide Menubar"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="166"` for all `Show/Hide Menubar` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="166" name="Show/Hide Menubar">
  
          
  <Lock state="True"/>
  
          
  <ShowHide value="Toggle"/>
  
        
</Step>

```
