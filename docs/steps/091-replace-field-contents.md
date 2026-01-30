---
id: 91
name: "Replace Field Contents"
category: Fields
status: draft
input_patterns:
  - "Replace Field Contents [ ... ]"
fm_name: "Replace Field Contents"
xml:
  step_name: "Replace Field Contents"
  enable_default: True
  wrapper: step-only
---

## Description

reflects the user's choice of what to replace the specified

          fields contents with.
  is present when

           is "SerialNumbers".
  and  can

          optionally be used to control serial number generation.
  is present when  is "Calculation".

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Replace Field Contents"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="91"` for all `Replace Field Contents` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="None">
        </Step>
        <Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="CurrentContents">
          <Field name="f3" id="2" table="test"/>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="SerialNumbers">
          <SerialNumbers UseEntryOptions="False"
            InitialValue="0" Increment="1"
        UpdateEntryOptions="False"/>
          <Field name="f3" id="2" table="test"/>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="Calculation">
          <Calculation>
            <![CDATA[Abs ( f3 )]]>
          </Calculation>
          <Field name="f3" id="2" table="test"/>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
```
