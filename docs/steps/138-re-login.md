---
id: 138
name: "Re-Login"
category: Account
status: draft
input_patterns:
  - "Re-Login [ ... ]"
fm_name: "Re-Login"
xml:
  step_name: "Re-Login"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Re-Login

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Re-Login"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="138"` for all `Re-Login` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="138" name="Re-Login" enable="True">
          <NoInteract state="True"/>
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
