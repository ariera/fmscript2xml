---
id: 182
name: "Truncate Table"
category: Records
status: draft
version: newto15
input_patterns:
  - "Truncate Table [ ... ]"
fm_name: "Truncate Table"
xml:
  step_name: "Truncate Table"
  enable_default: True
  wrapper: step-only
---

## Description

If  is not "", the ID and name reflect the specified table.

## Mapping rules

- `name="Truncate Table"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="182"` for all `Truncate Table` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="182" name="Truncate Table">
  
           
  <NoInteract state="False"/>
  
           
  <BaseTable id="-1" name="&lt;Current Table&gt;"/>
  
        
</Step>

```
