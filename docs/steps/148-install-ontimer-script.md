---
id: 148
name: "Install OnTimer Script"
category: Control
status: draft
input_patterns:
  - "Install OnTimer Script [ ... ]"
fm_name: "Install OnTimer Script"
xml:
  step_name: "Install OnTimer Script"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Install OnTimer Script

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Install OnTimer Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="148"` for all `Install OnTimer Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="148" name="Install OnTimer Script">
  
 
  <Interval>
    
          
    <Calculation>
          CalcString
          </Calculation>
    
          
  </Interval>
  

  <Script id="1" name="Script Name "/>
  

</Step>

```
