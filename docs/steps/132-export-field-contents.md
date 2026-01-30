---
id: 132
name: "Export Field Contents"
category: Fields
status: draft
input_patterns:
  - "Export Field Contents [ ... ]"
fm_name: "Export Field Contents"
xml:
  step_name: "Export Field Contents"
  enable_default: True
  wrapper: step-only
---

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Export Field Contents"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="132"` for all `Export Field Contents` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="132" name="Export Field Contents">
  
          
  <AutoOpen state="True"/>
  
          
  <CreateEmail state="True"/>
  
          
  <CreateDirectories state="True"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
          
  <Field name="FieldName" id="2" table="TableName"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```
