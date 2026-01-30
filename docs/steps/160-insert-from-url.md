---
id: 160
name: "Insert from URL"
category: Fields
status: draft
input_patterns:
  - "Insert from URL [ ... ]"
fm_name: "Insert from URL"
xml:
  step_name: "Insert from URL"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Insert from URL

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert from URL"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="160"` for all `Insert from URL` steps.
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
<Step enable="True" id="160" name="Insert from URL">
  
            
  <NoInteract state="True"/>
  
            
  <SelectAll state="True"/>
  
            
  <VerifySSLCertificates state="True"/>
  
  
  <DontEncodeURL state="False"/>
  
            
  <Calculation>
               &quot;Value&quot;
            </Calculation>
  
            ...
             ...
            
  <CURLOptions>
    
             
    <Calculation>&quot;Value&quot;</Calculation>
    
            
  </CURLOptions>
  

</Step>

```
