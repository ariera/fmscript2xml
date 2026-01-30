---
id: 96
name: "#[OBSOLETE]Update Link"
category: Fields
status: draft
input_patterns:
  - "#[OBSOLETE]Update Link [ ... ]"
fm_name: "#[OBSOLETE]Update Link"
xml:
  step_name: "#[OBSOLETE]Update Link"
  enable_default: True
  wrapper: step-only
---

## Description

It is no longer possible to create this script; although, you can have step in a converted file.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="#[OBSOLETE]Update Link"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="96"` for all `#[OBSOLETE]Update Link` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="96" name="#[OBSOLETE]Update Link">
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
