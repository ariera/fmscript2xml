---
id: 10
name: "Delete All Records"
category: Records
status: draft
input_patterns:
  - "Delete All Records [ ... ]"
fm_name: "Delete All Records"
xml:
  step_name: "Delete All Records"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Delete All Records

## Mapping rules

- `name="Delete All Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="10"` for all `Delete All Records` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="10" name="Delete All Records">
  
          
  <NoInteract state="True"/>
  
        
</Step>

```
