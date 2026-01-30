---
id: 185
name: "Configure Region Monitor Script"
category: Control
status: draft
version: newto16
input_patterns:
  - "Configure Region Monitor Script [ ... ]"
fm_name: "Configure Region Monitor Script"
xml:
  step_name: "Configure Region Monitor Script"
  enable_default: True
  wrapper: step-only
---

## Description

When  is Clear, only  is output.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Configure Region Monitor Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="185"` for all `Configure Region Monitor Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{value}` - appears conditionally
  - `{For an iBeacon monitor:
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="FunctionRef">Abs</Chunk>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              <MajorID>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="FunctionRef">Abs</Chunk>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </MajorID>
              <MinorID>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="FunctionRef">Abs</Chunk>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </MinorID>
              }` - appears conditionally
  - `{For a Geofence monitor:
              <Latitude>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="FunctionRef">Abs</Chunk>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </Latitude>
              <Longitude>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="FunctionRef">Abs</Chunk>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </Longitude>
              <Radius>
                 <Calculation><![CDATA[CalcString]]></Calculation>
                 <DisplayCalculation>
                    <Chunk type="FunctionRef">Abs</Chunk>
                    <Chunk type="NoRef">(13)</Chunk>
                 </DisplayCalculation>
              </Radius>
              }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="185" name="Configure Region Monitor Script">
  
           
  <Script id="156" name="Foo"/>
  
           
  <MonitorType value="...">
    
              
    <RangeName>
      
                 
      <Calculation>&quot;CalcString&quot;</Calculation>
      
              
    </RangeName>
    
              ...
              ...
           
  </MonitorType>
  
        
</Step>

```
