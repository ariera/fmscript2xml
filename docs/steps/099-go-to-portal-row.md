---
id: 99
name: "Go to Portal Row"
category: Navigation
status: draft
input_patterns:
  - "Go to Portal Row [ ... ]"
fm_name: "Go to Portal Row"
xml:
  step_name: "Go to Portal Row"
  enable_default: True
  wrapper: step-only
---

## Description

and  nodes are present when

           attribute is "ByCalculation".
  element is only present when  is

          "Next" or "Previous".
  indicates whether script execution should be terminated if

          there is no next/previous row in the portal (that is, if the current row is the

          last/first one in the portal).

## Mapping rules

- `name="Go to Portal Row"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="99"` for all `Go to Portal Row` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="99" name="Go to Portal Row">
  
           
  <NoInteract state="True"/>
  
           
  <SelectAll state="False"/>
  
           
  <Exit state="False"/>
  
           
  <RowPageLocation value="ByCalculation"/>
  
           
  <Calculation>
              CalcString
           </Calculation>
  
        
</Step>

```
