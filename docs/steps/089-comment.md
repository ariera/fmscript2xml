---
id: 89
name: "Comment"
category: Miscellaneous
status: draft
input_patterns:
  - "Comment [ ... ]"
fm_name: "Comment"
xml:
  step_name: "Comment"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Comment

## Mapping rules

- `name="Comment"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="89"` for all `Comment` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="89" name="Comment">
  
          
  <Text>This is a comment</Text>
  
        
</Step>

```
