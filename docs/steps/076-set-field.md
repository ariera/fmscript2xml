---
id: 76
name: "Set Field"
category: Fields
status: draft
input_patterns:
  - "Set Field [ ... ]"
fm_name: "Set Field"
xml:
  step_name: "Set Field"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Field

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Set Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="76"` for all `Set Field` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="76" name="Set Field">
  
          
  <Field name="f1" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
