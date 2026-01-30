---
id: 18
name: "Check Selection"
category: Spelling
status: draft
input_patterns:
  - "Check Selection [ ... ]"
fm_name: "Check Selection"
xml:
  step_name: "Check Selection"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Check Selection

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Check Selection"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="18"` for all `Check Selection` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="18" name="Check Selection">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
