---
id: 102
name: "Flush Cache to Disk"
category: Miscellaneous
status: draft
input_patterns:
  - "Flush Cache to Disk [ ... ]"
fm_name: "Flush Cache to Disk"
xml:
  step_name: "Flush Cache to Disk"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Flush Cache to Disk

## Mapping rules

- `name="Flush Cache to Disk"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="102"` for all `Flush Cache to Disk` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="102" name="Flush Cache to Disk">
        </Step>

```
