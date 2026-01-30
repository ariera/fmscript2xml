---
id: 51
name: "Revert Record/Request"
category: Records
status: draft
input_patterns:
  - "Revert Record/Request [ ... ]"
fm_name: "Revert Record/Request"
xml:
  step_name: "Revert Record/Request"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Revert Record/Request

## Mapping rules

- `name="Revert Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="51"` for all `Revert Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="51" name="Revert Record/Request">
  
          
  <NoInteract state="True"/>
  
        
</Step>

```
