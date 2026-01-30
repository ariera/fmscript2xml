---
id: 126
name: "Constrain Found Set"
category: Found Sets
status: draft
input_patterns:
  - "Constrain Found Set [ ... ]"
fm_name: "Constrain Found Set"
xml:
  step_name: "Constrain Found Set"
  enable_default: True
  wrapper: step-only
---

## Description

{See Perform Find}

## Mapping rules

- `name="Constrain Found Set"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="126"` for all `Constrain Found Set` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Perform Find}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="126" name="Constrain Found Set">
           ...
        </Step>

```
