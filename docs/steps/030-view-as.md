---
id: 30
name: "View As"
category: Windows
status: draft
input_patterns:
  - "View As [ ... ]"
fm_name: "View As"
xml:
  step_name: "View As"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: View As

## Mapping rules

- `name="View As"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="30"` for all `View As` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="30" name="View As">
  
           
  <View value="Form"/>
  
        
</Step>

```
