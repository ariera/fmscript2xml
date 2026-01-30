---
id: 64
name: "Send DDE Execute"
category: Miscellaneous
status: draft
input_patterns:
  - "Send DDE Execute [ ... ]"
fm_name: "Send DDE Execute"
xml:
  step_name: "Send DDE Execute"
  enable_default: True
  wrapper: step-only
---

## Description

is present when  is "File"

          and  is present when it is "Calculation".
{PathList} can consist of multiple absolute or relative paths, the first valid

          one of which is used at execution time.

## Mapping rules

- `name="Send DDE Execute"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="64"` for all `Send DDE Execute` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="64" name="Send DDE Execute">
          <ContentType value="Calculation">
          <UniversalPathList>...</UniversalPathList>
          <ServiceName>
            <Calculation>
              <![CDATA["Word"]]>
            </Calculation>
          </ServiceName>
          <Topic>
            <Calculation>
              <![CDATA["TopicText"]]>
            </Calculation>
          </Topic>
          <Command>
            <Calculation>
              <![CDATA["Delete All"]]>
            </Calculation>
          </Command>
        </Step>
```
