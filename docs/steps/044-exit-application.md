---
id: 44
name: "Exit Application"
category: Miscellaneous
status: draft
input_patterns:
  - "Exit Application [ ... ]"
fm_name: "Exit Application"
xml:
  step_name: "Exit Application"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Exit Application

## Mapping rules

- `name="Exit Application"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="44"` for all `Exit Application` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="44" name="Exit Application">
        </Step>

```
