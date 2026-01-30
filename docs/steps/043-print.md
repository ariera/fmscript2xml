---
id: 43
name: "Print"
category: Sort/Find/Print
status: draft
input_patterns:
  - "Print [ ... ]"
fm_name: "Print"
xml:
  step_name: "Print"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Print

## Mapping rules

- `name="Print"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="43"` for all `Print` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Flattened Windows/Mac specific
        settings}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="43" name="Print">
          <NoInteract state="True"/>
          <Restore state="true">
              <![CDATA[...]]>
        </Step>
```
