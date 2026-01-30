---
id: 57
name: "Send event"
category: Miscellaneous
status: draft
input_patterns:
  - "Send event [ ... ]"
fm_name: "Send event"
xml:
  step_name: "Send event"
  enable_default: True
  wrapper: step-only
---

## Description

is present when  is "File",

           is present when it is "Calculation", and  is

          present when it is "Text".
{PathList} can consist of multiple absolute or relative paths, the first valid

          one of which is used at execution time.

## Mapping rules

- `name="Send event"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="57"` for all `Send event` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally
  - `{CalcString}` - appears conditionally
  - `{TextString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="57" name="Send event">
          <ContentType value="Calculation">
          <UniversalPathList>...</UniversalPathList>
          <Calculation>...</Calculation>
          <Text>...</Text>
          <Event class=... id=...
             TargetName=... TargetType=...
             BringTargetToForeground="True"
        WaitForCompletion="True"
             CopyResultToClipBoard="False"/>
        </Step>
```
