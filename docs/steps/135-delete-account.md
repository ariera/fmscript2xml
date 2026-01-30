---
id: 135
name: "Delete Account"
category: Account
status: draft
input_patterns:
  - "Delete Account [ ... ]"
fm_name: "Delete Account"
xml:
  step_name: "Delete Account"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Delete Account

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Delete Account"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="135"` for all `Delete Account` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="135" name="Delete Account" enable="True">
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
        </Step>
```
