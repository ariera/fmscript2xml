---
id: 116
name: "Set Next Serial Value"
category: Fields
status: draft
input_patterns:
  - "Set Next Serial Value [ ... ]"
fm_name: "Set Next Serial Value"
xml:
  step_name: "Set Next Serial Value"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Set Next Serial Value

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Set Next Serial Value"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="116"` for all `Set Next Serial Value` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="116" name="Set Next Serial Value">
  
          
  <Calculation>
            12
          </Calculation>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
