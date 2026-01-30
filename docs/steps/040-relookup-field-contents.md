---
id: 40
name: "Relookup Field Contents"
category: Fields
status: draft
input_patterns:
  - "Relookup Field Contents [ ... ]"
fm_name: "Relookup Field Contents"
xml:
  step_name: "Relookup Field Contents"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Relookup Field Contents

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Relookup Field Contents"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="40"` for all `Relookup Field Contents` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="40" name="Relookup Field Contents">
  
          
  <NoInteract state="True"/>
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
