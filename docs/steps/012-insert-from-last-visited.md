---
id: 12
name: "Insert from Last Visited"
category: Fields
status: draft
input_patterns:
  - "Insert from Last Visited [ ... ]"
fm_name: "Insert from Last Visited"
xml:
  step_name: "Insert from Last Visited"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Insert from Last Visited

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert from Last Visited"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="12"` for all `Insert from Last Visited` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="12" name="Insert from Last Visited">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
