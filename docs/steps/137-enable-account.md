---
id: 137
name: "Enable Account"
category: Account
status: draft
input_patterns:
  - "Enable Account [ ... ]"
fm_name: "Enable Account"
xml:
  step_name: "Enable Account"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Enable Account

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Enable Account"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="137"` for all `Enable Account` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="137" name="Enable Account" enable="True">
          <AccountOperation value="Activate"/>
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
        </Step>
```
