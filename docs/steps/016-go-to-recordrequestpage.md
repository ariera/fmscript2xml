---
id: 16
name: "Go to Record/Request/Page"
category: Navigation
status: draft
input_patterns:
  - "Go to Record/Request/Page [ ... ]"
fm_name: "Go to Record/Request/Page"
xml:
  step_name: "Go to Record/Request/Page"
  enable_default: True
  wrapper: step-only
---

## Description

and  nodes are present when

         attribute is "ByCalculation".



         element is only present when  is

        "Next" or "Previous".



         indicates whether script execution should be terminated if

        there is no next/previous record/request/page (that is, if the current

        record/request/page is the last/first one).

## Mapping rules

- `name="Go to Record/Request/Page"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="16"` for all `Go to Record/Request/Page` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="16" name="Go to Record/Request/Page">
  
          
  <NoInteract state="True"/>
  
          
  <Exit state="False"/>
  
          
  <RowPageLocation value="ByCalculation"/>
  
          
  <Calculation>
             CalcString
          </Calculation>
  
        
</Step>

```
