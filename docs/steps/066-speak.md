---
id: 66
name: "Speak"
category: Miscellaneous
status: draft
input_patterns:
  - "Speak [ ... ]"
fm_name: "Speak"
xml:
  step_name: "Speak"
  enable_default: True
  wrapper: step-only
---

## Description

is only generated on the Mac and contains redundant information that only

        serves to make DDR reports (in particular HTML ones) more readable.

## Mapping rules

- `name="Speak"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="66"` for all `Speak` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{voice creator}` - appears conditionally
  - `{voice
        id}` - appears conditionally
  - `{voice name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="66" name="Speak">
           <SpeechOptions VoiceCreator=... VoiceId=...
              VoiceName=...
        WaitForCompletion="True"/>
           <Calculation>
             <![CDATA[CalcString]]>
           </Calculation>
        </Step>
```
