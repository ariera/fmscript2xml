---
id: 32
name: "Open Help"
category: Open Menu Item
status: draft
input_patterns:
  - "Open Help [ ... ]"
fm_name: "Open Help"
xml:
  step_name: "Open Help"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Open Help

## Mapping rules

- `name="Open Help"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="32"` for all `Open Help` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="32" name="Open Help">
        </Step>

```
