---
id: 28
name: "Perform Find"
category: Found Sets
status: draft
input_patterns:
  - "Perform Find [ ... ]"
fm_name: "Perform Find"
xml:
  step_name: "Perform Find"
  enable_default: True
  wrapper: step-only
---

## Description

Query node can have 1 or more RequestRow sub-nodes.
Each RequestRow node can in turn have 1 or more Criteria sub-nodes.
  contains the actual criteria itself that will be applied to

          . 
  is only output if > 1.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Perform Find"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="28"` for all `Perform Find` steps.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="28" name="Perform Find">
  
          
  <Restore state="True"/>
  
          
  <Query table="test123">
    
            
    <RequestRow operation="Include">
      
              
      <Criteria>
        
                
        <Text>&gt; 11</Text>
        
                
        <Field name="f2" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
              
      <Criteria>
        
                
        <Text>&lt; 23</Text>
        
                
        <Field name="f3" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
            
    </RequestRow>
    
            
    <RequestRow operation="Exclude">
      
              
      <Criteria>
        
                
        <Text>&gt;
        &quot;wow&quot;</Text>
        
                
        <Field name="f3" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
              
      <Criteria>
        
                
        <Text>&gt;
        test</Text>
        
                
        <Field name="f4" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
              
      <Criteria>
        
                
        <Text>&gt; &quot;hello
        there </Text>
        
                
        <Field name="f5" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
            
    </RequestRow>
    
          
  </Query>
  
        
</Step>

```
