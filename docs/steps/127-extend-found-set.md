---
id: 127
name: "Extend Found Set"
category: Found Sets
status: draft
input_patterns:
  - "Extend Found Set [ ... ]"
fm_name: "Extend Found Set"
xml:
  step_name: "Extend Found Set"
  enable_default: True
  wrapper: step-only
---

## Description

{See Perform Find}

## Mapping rules

- `name="Extend Found Set"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="127"` for all `Extend Found Set` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Perform Find}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="127" name="Extend Found Set">
           ...
        </Step>

```
