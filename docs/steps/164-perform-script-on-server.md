---
id: 164
name: "Perform Script on Server"
category: Control
status: draft
input_patterns:
  - "Perform Script on Server [ ... ]"
fm_name: "Perform Script on Server"
xml:
  step_name: "Perform Script on Server"
  enable_default: True
  wrapper: step-only
---

## Description

is only required for external scripts.
 exists only when a script name is specified by a calculation.
{PathList} can consist of multiple absolute or relative paths, the first valid

          one of which is used at execution time.
  and  nodes will only exist when a script parameter was specified.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Perform Script on Server"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="164"` for all `Perform Script on Server` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{name}` - appears conditionally
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="164" name="Perform Script on Server">
          <Calculated>
           <Calculation>
              <![CDATA["Script name"]]>
           </Calculation>
          </Calculated>
           <DisplayCalculation>
           <Calculation>
          <WaitForCompletion state="True"/>
          <FileReference name=... id="1">
            <UniversalPathList>...</UniversalPathList>
          </FileReference>
          <Script name="EndOfYear" id="1"/>
        </Step>
```
