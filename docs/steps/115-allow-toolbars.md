---
id: 115
name: "Allow Toolbars"
category: Miscellaneous
status: draft
input_patterns:
  - "Allow Toolbars [ ... ]"
fm_name: "Allow Toolbars"
xml:
  step_name: "Allow Toolbars"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Allow Toolbars

## Mapping rules

- `name="Allow Toolbars"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="115"` for all `Allow Toolbars` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="115" name="Allow Toolbars">
  
          
  <Set state="True"/>
  
        
</Step>

```
