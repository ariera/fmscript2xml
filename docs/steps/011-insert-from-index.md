---
id: 11
name: "Insert from Index"
category: Fields
status: draft
input_patterns:
  - "Insert from Index [ ... ]"
fm_name: "Insert from Index"
xml:
  step_name: "Insert from Index"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Insert from Index

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert from Index"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="11"` for all `Insert from Index` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="11" name="Insert from Index">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
