---
id: 47
name: "Copy"
category: Editing
status: draft
input_patterns:
  - "Copy [ ... ]"
fm_name: "Copy"
xml:
  step_name: "Copy"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Copy

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Copy"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="47"` for all `Copy` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="47" name="Copy">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
