---
id: 45
name: "Undo/Redo"
category: Editing
status: draft
input_patterns:
  - "Undo/Redo [ ... ]"
fm_name: "Undo/Redo"
xml:
  step_name: "Undo/Redo"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Undo/Redo

## Mapping rules

- `name="Undo/Redo"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="45"` for all `Undo/Redo` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="45" name="Undo/Redo">
  
          
  <UndoRedo value="Toggle"/>
  
        
</Step>

```
