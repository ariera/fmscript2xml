---
id: 85
name: "Allow User Abort"
category: Control
status: draft
input_patterns:
  - "Allow User Abort [ ... ]"
fm_name: "Allow User Abort"
xml:
  step_name: "Allow User Abort"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Allow User Abort

## Mapping rules

- `name="Allow User Abort"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="85"` for all `Allow User Abort` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="85" name="Allow User Abort">
  
          
  <Set state="True"/>
  
        
</Step>

```
