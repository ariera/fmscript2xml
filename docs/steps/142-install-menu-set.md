---
id: 142
name: "Install Menu Set"
category: Miscellaneous
status: draft
input_patterns:
  - "Install Menu Set [ ... ]"
fm_name: "Install Menu Set"
xml:
  step_name: "Install Menu Set"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Install Menu Set

## Mapping rules

- `name="Install Menu Set"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="142"` for all `Install Menu Set` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Menu set name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="142" name="Install Menu Set">
           <UseAsFileDefault state="True"/>
           <CustomMenuSet id="3" name=.../>
        </Step>
```
