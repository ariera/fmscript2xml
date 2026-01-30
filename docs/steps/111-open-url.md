---
id: 111
name: "Open URL"
category: Miscellaneous
status: draft
input_patterns:
  - "Open URL [ ... ]"
fm_name: "Open URL"
xml:
  step_name: "Open URL"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Open URL

## Mapping rules

- `name="Open URL"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="111"` for all `Open URL` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="111" name="Open URL">
  
          
  <NoInteract state="True"/>
  
          
  <Calculation>
            &quot;https://www.filemaker.com&quot;
          </Calculation>
  
        
</Step>

```
