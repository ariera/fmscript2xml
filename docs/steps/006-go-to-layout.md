---
id: 6
name: "Go to Layout"
category: Navigation
status: draft
input_patterns:
  - "Go to Layout [ ... ]"
fm_name: "Go to Layout"
xml:
  step_name: "Go to Layout"
  enable_default: True
  wrapper: step-only
---

## Description

element is output only if  is not "OriginalLayout."
  element is output only if  is "LayoutNameByCalc" or "LayoutNumberByCalc".
  is required in case there is more than one layout with the same name.
 element is output only if an animation value other than "None" was selected for the script step.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Go to Layout"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="6"` for all `Go to Layout` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Layout id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Layout>` element specifies the target layout.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{AnimationID}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="6" name="Go to Layout">
          <LayoutDestination value="SelectedLayout"/>
          <Layout name="LayoutName" id="1"/>
            <Calculation>
              <![CDATA[CalcString]]>
            </Calculation>
          </Layout>
  <Animation value=.../>
        </Step>
```
