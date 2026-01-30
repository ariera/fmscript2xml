---
id: 29
name: "Show/Hide Toolbars"
category: Windows
status: draft
input_patterns:
  - "Show/Hide Toolbars [ ... ]"
fm_name: "Show/Hide Toolbars"
xml:
  step_name: "Show/Hide Toolbars"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Show/Hide Toolbars

## Mapping rules

- `name="Show/Hide Toolbars"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="29"` for all `Show/Hide Toolbars` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="29" name="Show/Hide Toolbars">
  
          
  <Lock state="True"/>
  
          
  <ShowHide value="Hide"/>
  
        
</Step>

```
