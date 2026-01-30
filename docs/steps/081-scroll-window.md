---
id: 81
name: "Scroll Window"
category: Windows
status: draft
input_patterns:
  - "Scroll Window [ ... ]"
fm_name: "Scroll Window"
xml:
  step_name: "Scroll Window"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Scroll Window

## Mapping rules

- `name="Scroll Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="81"` for all `Scroll Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="81" name="Scroll Window">
  
          
  <ScrollOperation value="Home"/>
  
        
</Step>

```
