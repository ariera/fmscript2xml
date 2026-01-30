---
id: 144
name: "Save Records as PDF"
category: Records
status: draft
input_patterns:
  - "Save Records as PDF [ ... ]"
fm_name: "Save Records as PDF"
xml:
  step_name: "Save Records as PDF"
  enable_default: True
  wrapper: step-only
---

## Description

is generated only if
        
 is "BlankRecord"
 is "Append to Existing PDF"

## Mapping rules

- `name="Save Records as PDF"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="144"` for all `Save Records as PDF` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="144" name="Save Records as PDF">
          <Option state="True"/>
          <NoInteract state="True"/>
          <Restore state="True"/>
          <AutoOpen state="True"/>
          <CreateEmail state="True"/>
          <CreateDirectories state="True"/>
          <UniversalPathList>...</UniversalPathList>
            <Document compatibility="Acrobat5AndLater">
              <Title>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
               </Title>
                <Subject>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
                </Subject>
                <Author>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
                </Author >
                <KeyWords>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
                </KeyWords >
                <NumberFrom>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
                </NumberFrom>
                <AllPages state="true">
                <From>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
                </From>
                <To>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
                </To>
            </Document>
            <Security requireOpenPassword="True"
                requireControlEditPassword="True"
                controlPrinting="HighResolution"
                controlEditing="AnyExceptExtracting"
                enableCopying="True"
        allowScreenReader="True">
              <OpenPassword>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
               </OpenPassword>
              <ControlPassword>
                <Calculation>
                <![CDATA[CalcString]]>
                </Calculation>
              </ControlPassword>
            </Security>
            <View show="PageOnly" pageLayout="SinglePage"
        magnification="25"/>
        </Step>
```
