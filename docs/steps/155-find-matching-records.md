---
id: 155
name: "Find Matching Records"
category: Found Sets
status: draft
input_patterns:
  - "Find Matching Records [ ... ]"
fm_name: "Find Matching Records"
xml:
  step_name: "Find Matching Records"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Find Matching Records

## Mapping rules

- `name="Find Matching Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="155"` for all `Find Matching Records` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="155" name="Find Matching Records">
  
        
  <FindMatchingRecordsByField value="FindMatchingReplace"/>
  
        
</Step>

```
