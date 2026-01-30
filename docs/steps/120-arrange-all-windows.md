---
id: 120
name: "Arrange All Windows"
category: Windows
status: draft
input_patterns:
  - "Arrange All Windows [ ... ]"
fm_name: "Arrange All Windows"
xml:
  step_name: "Arrange All Windows"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Arrange All Windows

## Mapping rules

- `name="Arrange All Windows"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="120"` for all `Arrange All Windows` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="120" name="Arrange All Windows">
  
          
  <WindowArrangement value="TileHorizontally"/>
  
        
</Step>

```
