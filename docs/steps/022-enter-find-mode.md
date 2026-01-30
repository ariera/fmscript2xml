---
id: 22
name: "Enter Find Mode"
category: Navigation
status: draft
input_patterns:
  - "Enter Find Mode [ ... ]"
fm_name: "Enter Find Mode"
xml:
  step_name: "Enter Find Mode"
  enable_default: True
  wrapper: step-only
---

## Description

{See Perform Find.}

## Mapping rules

- `name="Enter Find Mode"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="22"` for all `Enter Find Mode` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Perform Find for remaining XML.}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="22" name="Enter Find Mode">
          ...
        <Step enable="True">
```
