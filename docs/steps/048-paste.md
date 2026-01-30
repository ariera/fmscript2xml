---
id: 48
name: "Paste"
category: Editing
status: draft
input_patterns:
  - "Paste [ ... ]"
fm_name: "Paste"
xml:
  step_name: "Paste"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Paste

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Paste"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="48"` for all `Paste` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="48" name="Paste">
  
          
  <NoStyle state="True"/>
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
