---
id: 74
name: "Go to Related Record"
category: Navigation
status: draft
input_patterns:
  - "Go to Related Record [ ... ]"
fm_name: "Go to Related Record"
xml:
  step_name: "Go to Related Record"
  enable_default: True
  wrapper: step-only
---

## Description

is used to denote state of "Use external table's layout'"

          checkbox.
  element is used to denote state of "Show all related records in

          new found set" checkbox.
  element is output only if  is not "CurrentLayout"
  element is output only if  is "LayoutNameByCalc" or "LayoutNumberByCalc."
 element is output only if an animation value other than "None" was selected for the script step.

## Mapping rules

- `name="Go to Related Record"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="74"` for all `Go to Related Record` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- `<Layout>` element specifies the target layout.
- `<Table>` element specifies the target table.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{TableName}` - appears conditionally
  - `{id value}` - appears conditionally
  - `{LayoutName}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="74" name="Go to Related Record">
          <Option state="true"/>
          <ShowInNewWindow state="true"/>
          <Restore state="true"/>
          <MatchAllRecords state="true"/>
          <Table name=... id=.../>
          <LayoutDestination value="SelectedLayout"/>
          <Layout name=... id=.../>
  <Animation value=.../>
          <Name>
              <Calculation><![CDATA[CalcString]]></Calculation>
          </Name>
          <Height>
              <Calculation><![CDATA[CalcString]]></Calculation>
          </Height>
          <Width>
              <Calculation><![CDATA[CalcString]]></Calculation>
          </Width>
          <DistanceFromTop>
              <Calculation><![CDATA[CalcString]]></Calculation>
          </DistanceFromTop>
          <DistanceFromLeft>
              <Calculation><![CDATA[1221]]></Calculation>
           </DistanceFromLeft>
        </Step>
```
