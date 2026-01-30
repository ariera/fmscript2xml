---
id: 130
name: "Set Selection"
category: Editing
status: draft
input_patterns:
  - "Set Selection [ ... ]"
fm_name: "Set Selection"
xml:
  step_name: "Set Selection"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Selection

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Set Selection"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="130"` for all `Set Selection` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally
  - `{FieldName}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="130" name="Set Selection">
          <StartPosition>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </StartPosition>
          <EndPosition>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </EndPosition>
          <Field name=... id="2" table=.../>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
```
