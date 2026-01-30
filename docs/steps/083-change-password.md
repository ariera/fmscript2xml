---
id: 83
name: "Change Password"
category: Account
status: draft
input_patterns:
  - "Change Password [ ... ]"
fm_name: "Change Password"
xml:
  step_name: "Change Password"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Change Password

## Mapping rules

- `name="Change Password"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="83"` for all `Change Password` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="83" name="Change Password">
  
          
  <NoInteract state="True"/>
  
          
  <OldPassword>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </OldPassword>
  
          
  <NewPassword>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </NewPassword>
  
        
</Step>

```
