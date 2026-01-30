---
id: 42
name: "Print Setup"
category: Sort/Find/Print
status: draft
input_patterns:
  - "Print Setup [ ... ]"
fm_name: "Print Setup"
xml:
  step_name: "Print Setup"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Print Setup

## Mapping rules

- `name="Print Setup"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="42"` for all `Print Setup` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Flattened Windows/Mac specific
        settings}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="42" name="Print Setup">
          <NoInteract state="False"/>
          <Restore state="true">
              <![CDATA[...]]>
          </Format>
        </Step>
```
