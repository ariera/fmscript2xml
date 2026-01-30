---
id: 17
name: "Go to Field"
category: Navigation
status: draft
input_patterns:
  - "Go to Field [ ... ]"
fm_name: "Go to Field"
xml:
  step_name: "Go to Field"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Go to Field

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Go to Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="17"` for all `Go to Field` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="17" name="Go to Field">
  
           
  <SelectAll state="True"/>
  
           
  <Field name="FieldName" id="2" table="TableName"/>
  
           
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
