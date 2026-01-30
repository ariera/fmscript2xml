---
id: 177
name: "AVPlayer Play"
category: Miscellaneous
status: draft
input_patterns:
  - "AVPlayer Play [ ... ]"
fm_name: "AVPlayer Play"
xml:
  step_name: "AVPlayer Play"
  enable_default: True
  wrapper: step-only
---

## Description

The AVPlayer script step is used to initiate the playing of media from a field (must be a container), a layout object (must be a container), URL, or the active object (must be a container). When creating the script step, a field chooser, object chooser, or URL text entry box will be shown as appropriate. All parameters are optional. Only one of the "Field", "Object", or "URL" parameters may be specified for a given step. Playback of the active object is initiated if layout object is specified and no layout object name is provided.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="AVPlayer Play"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="177"` for all `AVPlayer Play` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Script step text}` - appears conditionally
  - `{Table}` - appears conditionally
  - `{FieldName}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="177" name="AVPlayer Play">
          <Source value="Object">
            <Calculation><![CDATA["ObjectName"]]></Calculation>
          </Source>
          <Repetition>
            <Calculation><![CDATA[3]]></Calculation>
          </Repetition>
          <Source value="Field">
          <Field table=... name=... repetition="1" id="2" />
          </Source>
          <Source value="URL">
            <Calculation><![CDATA["MyURL"]]></Calculation>
          </Source>
          <HideControls value="True"/>
          <DisableInteraction value="True"/>
            <Calculation><![CDATA[30]]></Calculation>
          <StartOffset>
            <Calculation><![CDATA[20]]></Calculation>
          </StartOffset>
          <EndOffset>
            <Calculation><![CDATA[120]]></Calculation>
          </EndOffset>
        </Step>
```
