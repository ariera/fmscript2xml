---
id: 174
name: "Enable Touch Keyboard"
category: Windows
status: draft
input_patterns:
  - "Enable Touch Keyboard [ ... ]"
fm_name: "Enable Touch Keyboard"
xml:
  step_name: "Enable Touch Keyboard"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Enable Touch Keyboard

## Mapping rules

- `name="Enable Touch Keyboard"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="174"` for all `Enable Touch Keyboard` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="174" name="Enable Touch Keyboard">
  
            
  <ShowHide value="Hide"/>
  
        
</Step>

```
