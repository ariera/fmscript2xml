---
id: 13
name: "Insert Current Date"
category: Fields
status: draft
input_patterns:
  - "Insert Current Date [ ... ]"
fm_name: "Insert Current Date"
xml:
  step_name: "Insert Current Date"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Insert Current Date

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Current Date"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="13"` for all `Insert Current Date` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f3" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="13" name="Insert Current Date">
  
          
  <SelectAll state="True"/>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
