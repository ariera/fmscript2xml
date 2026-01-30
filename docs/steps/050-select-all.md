---
id: 50
name: "Select All"
category: Editing
status: draft
input_patterns:
  - "Select All [ ... ]"
fm_name: "Select All"
xml:
  step_name: "Select All"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Select All

## Mapping rules

- `name="Select All"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="50"` for all `Select All` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="50" name="Select All">
        </Step>

```
