---
id: 67
name: "Perform AppleScript"
category: Miscellaneous
status: draft
input_patterns:
  - "Perform AppleScript [ ... ]"
fm_name: "Perform AppleScript"
xml:
  step_name: "Perform AppleScript"
  enable_default: True
  wrapper: step-only
---

## Description

is present when  is "Calculation"

        and  is present when it is "Text".

## Mapping rules

- `name="Perform AppleScript"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="67"` for all `Perform AppleScript` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{compiled apple script data}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="67" name="Perform AppleScript">
          <ContentType value="Calculation">
          <CompiledScript>
            <![CDATA[...]]>
          </CompiledScript>
          <Calculation>
            <![CDATA["this is a calculated string"]]>
          </Calculation>
          <Text>This is a string literal</Text>
        </Step>
```
