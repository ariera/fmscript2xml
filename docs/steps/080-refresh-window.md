---
id: 80
name: "Refresh Window"
category: Windows
status: draft
input_patterns:
  - "Refresh Window [ ... ]"
fm_name: "Refresh Window"
xml:
  step_name: "Refresh Window"
  enable_default: True
  wrapper: step-only
---

## Description

corresponds to the "flush cached join results" option.
 corresponds to the "flush cached SQL data" option.

## Mapping rules

- `name="Refresh Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="80"` for all `Refresh Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="80" name="Refresh Window">
  
          
  <Option state="True"/>
  
          
  <FlushSQLData state="True"/>
  
        
</Step>

```
