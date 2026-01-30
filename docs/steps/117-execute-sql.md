---
id: 117
name: "Execute SQL"
category: Miscellaneous
status: draft
input_patterns:
  - "Execute SQL [ ... ]"
fm_name: "Execute SQL"
xml:
  step_name: "Execute SQL"
  enable_default: True
  wrapper: step-only
---

## Description

{See ODBC data source profile element in Import Records step}

## Mapping rules

- `name="Execute SQL"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="117"` for all `Execute SQL` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See ODBC data source profile element in Import Records step}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="117" name="Execute SQL">
  
          
  <NoInteract state="True"/>
  
          ...
        
</Step>

```
