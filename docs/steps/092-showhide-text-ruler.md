---
id: 92
name: "Show/Hide Text Ruler"
category: Windows
status: draft
input_patterns:
  - "Show/Hide Text Ruler [ ... ]"
fm_name: "Show/Hide Text Ruler"
xml:
  step_name: "Show/Hide Text Ruler"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Show/Hide Text Ruler

## Mapping rules

- `name="Show/Hide Text Ruler"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="92"` for all `Show/Hide Text Ruler` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="92" name="Show/Hide Text Ruler">
  
          
  <ShowHide value="Hide"/>
  
        
</Step>

```
