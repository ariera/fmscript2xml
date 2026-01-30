---
id: 136
name: "Reset Account Password"
category: Account
status: draft
input_patterns:
  - "Reset Account Password [ ... ]"
fm_name: "Reset Account Password"
xml:
  step_name: "Reset Account Password"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Reset Account Password

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Reset Account Password"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="136"` for all `Reset Account Password` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="136" name="Reset Account Password" enable="True">
          <ChgPwdOnNextLogin value="True">
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
        </Step>
```
