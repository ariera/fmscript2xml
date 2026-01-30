---
id: 134
name: "Add Account"
category: Account
status: draft
input_patterns:
  - "Add Account [ ... ]"
fm_name: "Add Account"
xml:
  step_name: "Add Account"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Add Account

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Add Account"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="134"` for all `Add Account` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="134" name="Add Account" enable="True">
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
