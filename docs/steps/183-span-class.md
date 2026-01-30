---
id: 183
name: "<span class="
category: Open Menu Item
status: draft
version: newto16
input_patterns:
  - "<span class= [ ... ]"
fm_name: "<span class="
xml:
  step_name: "<span class="
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: <span class=

## Mapping rules

- `name="<span class="` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="183"` for all `<span class=` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="183" name="Open My Apps">
        </Step>

```
