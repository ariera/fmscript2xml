---
id: 183
name: "Open My Apps"
category: Open Menu Item
status: draft
version: newto16
input_patterns:
  - "Open My Apps [ ... ]"
fm_name: "Open My Apps"
xml:
  step_name: "Open My Apps"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Open My Apps

## Mapping rules

- `name="Open My Apps"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="183"` for all `Open My Apps` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="183" name="Open My Apps">
        </Step>

```
