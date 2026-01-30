---
id: 62
name: "Pause/Resume Script"
category: Control
status: draft
input_patterns:
  - "Pause/Resume Script [ ... ]"
fm_name: "Pause/Resume Script"
xml:
  step_name: "Pause/Resume Script"
  enable_default: True
  wrapper: step-only
---

## Description

node exists when  is "ForDuration".

## Mapping rules

- `name="Pause/Resume Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="62"` for all `Pause/Resume Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="62" name="Pause/Resume Script">
  
           
  <Calculation>
              120
           </Calculation>
  
        
</Step>

```
