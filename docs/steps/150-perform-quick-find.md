---
id: 150
name: "Perform Quick Find"
category: Found Sets
status: draft
input_patterns:
  - "Perform Quick Find [ ... ]"
fm_name: "Perform Quick Find"
xml:
  step_name: "Perform Quick Find"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Perform Quick Find

## Mapping rules

- `name="Perform Quick Find"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="150"` for all `Perform Quick Find` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="150" name="Perform Quick Find">
          <Calculation>
            <! [CDATA[ "Value" ]] >
          </Calculation>
        </Step>
```
