---
id: 88
name: "Open Script Workspace"
category: Open Menu Item
status: draft
input_patterns:
  - "Open Script Workspace [ ... ]"
fm_name: "Open Script Workspace"
xml:
  step_name: "Open Script Workspace"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Open Script Workspace

## Mapping rules

- `name="Open Script Workspace"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="88"` for all `Open Script Workspace` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="88" name="Open Script Workspace">
        </Step>

```
