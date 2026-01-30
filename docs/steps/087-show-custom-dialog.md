---
id: 87
name: "Show Custom Dialog"
category: Miscellaneous
status: draft
input_patterns:
  - "Show Custom Dialog [ ... ]"
fm_name: "Show Custom Dialog"
xml:
  step_name: "Show Custom Dialog"
  enable_default: True
  wrapper: step-only
---

## Description

is only output if > 1

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Show Custom Dialog"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="87"` for all `Show Custom Dialog` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally
  - `{For a field as the target:
              <Field name={FieldName}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="87" name="Show Custom Dialog">
          <Title>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </Title>
          <Message>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </Message>
  <Buttons>
              <Button CommitState="True">
                 <Calculation>
                   <![CDATA["OK"]]>
                 </Calculation>
              </Button>
              <Button CommitState="False">
                 <Calculation>
                   <![CDATA["Cancel"]]>
                 </Calculation>
              </Button>
              <Button CommitState="False">
                 <Calculation>
                   <![CDATA[Get( CurrentTime )]]>
                 </Calculation>
              </Button>
            </Buttons>
          <InputFields>
            <InputField
        UsePasswordCharacter="True">
              ... id="2" repetition="2" table=.../>
              }
              ...
              <Label>
                <Calculation>
                <![CDATA[...]]>
                </Calculation>
              </Label>
            <InputField>
            ...
            </InputField>
            ...
          </InputFields>
        </Step>
```
