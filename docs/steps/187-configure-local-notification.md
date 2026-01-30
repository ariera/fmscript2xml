---
id: 187
name: "Configure Local Notification"
category: Control
status: draft
version: newto17
input_patterns:
  - "Configure Local Notification [ ... ]"
fm_name: "Configure Local Notification"
xml:
  step_name: "Configure Local Notification"
  enable_default: True
  wrapper: step-only
---

## Description

When  is Clear, only  is output.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Configure Local Notification"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="187"` for all `Configure Local Notification` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{value}` - appears conditionally
  - `{
              <Delay>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </Delay>
              <Title>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </Title>
              <Body>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </Body>
              <Button1Label>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">"Btn 1 Label"</Chunk>
                 </DisplayCalculation>
              </Button1Label>
              <Button2Label>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">"Btn 2 Label"</Chunk>
                 </DisplayCalculation>
              </Button2Label>
              <Button3Label>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">"Btn 3 Label"</Chunk>
                 </DisplayCalculation>
              </Button3Label>
              <Button1ForceFgnd>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">1</Chunk>
                 </DisplayCalculation>
              </Button1ForceFgnd>
              <Button2ForceFgnd>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">0</Chunk>
                 </DisplayCalculation>
              </Button2ForceFgnd>
              <Button3ForceFgnd>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="NoRef">1</Chunk>
                 </DisplayCalculation>
              </Button3ForceFgnd>
              }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="187" name="Configure Local Notification">
  
           
  <Script id="3" name="Custom Dialog"/>
  
           
  <Action value="...">
    
              
    <Name>
      
                 
      <Calculation>&quot;CalcString&quot;</Calculation>
      
              
    </Name>
    
              For Action == Queue:
              ...
           
  </Action>
  
        
</Step>

```
