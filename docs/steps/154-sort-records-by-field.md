---
id: 154
name: "Sort Records by Field"
category: Found Sets
status: draft
input_patterns:
  - "Sort Records by Field [ ... ]"
fm_name: "Sort Records by Field"
xml:
  step_name: "Sort Records by Field"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Sort Records by Field

## Mapping rules

- `name="Sort Records by Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="154"` for all `Sort Records by Field` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="154" name="Sort Records by Field">
  
        
  <SortRecordsByField value="SortAscending"/>
  
        
</Step>

```
