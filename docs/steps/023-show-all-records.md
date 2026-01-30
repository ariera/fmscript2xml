---
id: 23
name: "Show All Records"
category: Found Sets
status: draft
input_patterns:
  - "Show All Records [ ... ]"
fm_name: "Show All Records"
xml:
  step_name: "Show All Records"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Show All Records

## Mapping rules

- `name="Show All Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="23"` for all `Show All Records` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="23" name="Show All Records">
        </Step>

```
