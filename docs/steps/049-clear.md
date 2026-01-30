---
id: 49
name: "Clear"
category: Editing
status: draft
input_patterns:
  - "Clear [ ... ]"
fm_name: "Clear"
xml:
  step_name: "Clear"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Clear

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Clear"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="49"` for all `Clear` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="49" name="Clear">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f4" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
