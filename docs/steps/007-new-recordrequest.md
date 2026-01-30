---
id: 7
name: "New Record/Request"
category: Records
status: draft
input_patterns:
  - "New Record/Request [ ... ]"
fm_name: "New Record/Request"
xml:
  step_name: "New Record/Request"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: New Record/Request

## Mapping rules

- `name="New Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="7"` for all `New Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="7" name="New Record/Request">
        </Step>

```
