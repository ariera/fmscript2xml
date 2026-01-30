---
id: 75
name: "Commit Records/Requests"
category: Records
status: draft
input_patterns:
  - "Commit Records/Requests [ ... ]"
fm_name: "Commit Records/Requests"
xml:
  step_name: "Commit Records/Requests"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Commit Records/Requests

## Mapping rules

- `name="Commit Records/Requests"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="75"` for all `Commit Records/Requests` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="75" name="Commit Records/Requests">
  
          
  <NoInteract state="True"/>
  
          
  <Option state="true"/>
  
        
  <ESSForceCommit state="True"/>
   
</Step>

```
