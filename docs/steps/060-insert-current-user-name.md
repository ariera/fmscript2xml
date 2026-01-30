---
id: 60
name: "Insert Current User Name"
category: Fields
status: draft
input_patterns:
  - "Insert Current User Name [ ... ]"
fm_name: "Insert Current User Name"
xml:
  step_name: "Insert Current User Name"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Insert Current User Name

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Current User Name"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="60"` for all `Insert Current User Name` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f4" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="60" name="Insert Current User Name">
  
          
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
