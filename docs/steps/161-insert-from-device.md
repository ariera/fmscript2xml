---
id: 161
name: "Insert from Device"
category: Fields
status: draft
input_patterns:
  - "Insert from Device [ ... ]"
fm_name: "Insert from Device"
xml:
  step_name: "Insert from Device"
  enable_default: True
  wrapper: step-only
---

## Description

FileMaker script step: Insert from Device

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert from Device"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="161"` for all `Insert from Device` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="161" name="Insert from Device">
           <InsertFrom value="Music Library"/>
           <Field name="f1" id="2" table="test"/>
           <Repetition>
              <Calculation>
                 <![CDATA["Value"]]>
              </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="161" name="Insert from Device">
           <InsertFrom value="Photo Library">
           <Field name="f1" id="2" table="test"/>
           <Repetition>
              <Calculation>
                 <![CDATA["Value"]]>
              </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="161" name="Insert from Device">
           <InsertFrom value="Camera">
           <DeviceOptions>
           <Camera Choice="front"|"Back"/>
           <Resolution Choice="full"|"small"|"medium"|"large"/>
           </DeviceOptions>
           <Field name="f1" id="2" table="test"/>
           <Repetition>
              <Calculation>
                 <![CDATA["Value"]]>
              </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="161" name="Insert from Device">
           <InsertFrom value="Video Camera"/StepText>
           <DeviceOptions>
           <Camera Choice="front"|"Back"/>
           <Resolution Choice="full"|"small"|"medium"|"large"/>
           <MaxDuration Enabled="true"|"false">
              <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
           </MaxDuration>
           <StartImmediately Enabled="true"|"false" />
           </DeviceOptions>
           <Field name="f1" id="2" table="test"/>
           <Repetition>
              <Calculation>
                 <![CDATA["Value"]]>
              </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="161" name="Insert from Device">
           <InsertFrom value="Microphone">
           <DeviceOptions>
           <MaxDuration Enabled="true"|"false">
              <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
           </MaxDuration>
           <StartImmediately Enabled="true"|"false" />
           </DeviceOptions>
           <Field name="f1" id="2" table="test"/>
           <Repetition>
              <Calculation>
                 <![CDATA["Value"]]>
              </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="161" name="Insert from Device">
           <InsertFrom value="Bar Code"/StepText>
           <DeviceOptions>
           <ScanFrom Type="Camera"|"Field"/>
           <Camera Choice="front"|"Back"/>
           <BarCodes Types=<barcode_bitmask32>/>
           </DeviceOptions>
           <Field name="f1" id="2" table="test"/>
           <Repetition>
              <Calculation>
                 <![CDATA["Value"]]>
              </Calculation>
           </Repetition>
           <ScanFrom>
              <Field name="f1" id="2" table="test"/>
              <Repetition>
                 <Calculation>
                    <![CDATA["Value"]]>
                 </Calculation>
              </Repetition>
           </ScanFrom>
        </Step>
        <Step enable="True" id="161" name="Insert from Device">
           <InsertFrom value="Signature">
           <Field name="f1" id="2" table="test"/>
           <Repetition>
              <Calculation>
                 <![CDATA["Value"]]>
              </Calculation>
           </Repetition>
    <DeviceOptions>
                <Title>
                   <Calculation>
          <![CDATA["Value"]]></Calculation>
                </Title>
                <Message>
                   <Calculation>
          <![CDATA["Value"]]></Calculation>
                </Message>
                   <Calculation>
          <![CDATA["Value"]]></Calculation>
             </DeviceOptions>
        </Step>
```
