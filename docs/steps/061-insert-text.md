---
id: 61
name: "Insert Text"
category: Fields
status: draft
input_patterns:
  - "Insert Text [ ... ]"
fm_name: "Insert Text"
xml:
  step_name: "Insert Text"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Insert Text

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Text"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="61"` for all `Insert Text` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f1" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="61" name="Insert Text">
  
          
  <SelectAll state="True"/>
  
          
  <Text>&quot;Text to insert&quot;</Text>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
