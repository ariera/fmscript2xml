---
id: 9
name: "Delete Record/Request"
category: Records
status: draft
input_patterns:
  - "Delete Record/Request [ ... ]"
fm_name: "Delete Record/Request"
xml:
  step_name: "Delete Record/Request"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Delete Record/Request

## Mapping rules

- `name="Delete Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="9"` for all `Delete Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="9" name="Delete Record/Request">
  
          
  <NoInteract state="True"/>
  
        
</Step>

```
