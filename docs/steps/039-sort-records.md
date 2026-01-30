---
id: 39
name: "Sort Records"
category: Found Sets
status: draft
input_patterns:
  - "Sort Records [ ... ]"
fm_name: "Sort Records"
xml:
  step_name: "Sort Records"
  enable_default: True
  wrapper: step-only
---

## Description

node exists if  is Custom
  and  sub-nodes are optional.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Sort Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="39"` for all `Sort Records` steps.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="39" name="Sort Records">
  
          
  <NoInteract state="False"/>
  
          
  <Restore state="True"/>
  
          
  <SortList>
    
            
    <Sort type="Descending">
      
                
      <Field name="f1" id="1" table="test123"/>
      
            
    </Sort>
    
            
    <Sort type="Ascending">
      
                
      <Field name="f4" id="2" table="test123"/>
      
              
      <SummaryField>
        
                
        <Field name="summary" id="3" table="test123"/>
        
              
      </SummaryField>
      
              
      <OverrideLanguage language="Japanese"/>
      
            
    </Sort>
    
            
    <Sort type="Custom">
      
                
      <Field name="f5" id="4" table="test123"/>
      
              
      <ValueList name="New Value List" id="1"/>
      
            
    </Sort>
    
          
  </SortList>
  
        
</Step>

```
