---
id: 65
name: "Dial Phone"
category: Miscellaneous
status: draft
input_patterns:
  - "Dial Phone [ ... ]"
fm_name: "Dial Phone"
xml:
  step_name: "Dial Phone"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Dial Phone

## Mapping rules

- `name="Dial Phone"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="65"` for all `Dial Phone` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="65" name="Dial Phone">
  
          
  <NoInteract state="True"/>
  
          
  <UseDialPreferences value="True"/>
  
          
  <Calculation>
            613-667-5030
          </Calculation>
  
        
</Step>

```
