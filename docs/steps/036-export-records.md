---
id: 36
name: "Export Records"
category: Records
status: draft
input_patterns:
  - "Export Records [ ... ]"
fm_name: "Export Records"
xml:
  step_name: "Export Records"
  enable_default: True
  wrapper: step-only
---

## Description

is only present if  is "XSLFile"
  is only present if  is "XSLHttp"
  is only present if  is "XSLCalculation"
{PathList} can consist of multiple absolute or relative paths, the first valid

          one of which is used at execution time.
  node normally contains only one  sub-node

          (identifying a field to be exported) but will contain a second one if the first

          is a summary field and the user requested that exported records be grouped by

          some field, in which case the second field is a "summarize by" field.
  is only output if > 1

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Export Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="36"` for all `Export Records` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{for non XML file data source (specified in UniversalPathList) :
        }` - appears conditionally
  - `{for XML file data source (specified in UniversalPathList) :
            <XSLFile>
              <UniversalPathList>{PathList}` - appears conditionally
  - `{http}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="36" name="Export Records">
          <NoInteract state="True"/>
          <Restore state="True"/>
          <AutoOpen state="True"/>
          <CreateEmail state="True"/>
          <CreateDirectories state="True"/>
        ...
        ...</UniversalPathList>
           </XSLFile>
            <XSLHttp>...</XSLHttp>
            <XSLCalc>
              <Calculation>
                <![CDATA[CalcString]]>
              </Calculation>
            </XSLCalc>
        }
        ...
          <UniversalPathList>...</UniversalPathList>
          <CreateDirectories state="True"/>
          <ExportOptions
            CharacterSet="Windows"/>
            FormatUsingCurrentLayout="True"/>
          </ExportOptions>
          <ExportEntries>
            <ExportEntry>
              <Field name=... id="2"
        repetition="2" table=.../>
              <Field name=... id="2"
        repetition="2" table=.../>
            </ExportEntry>
            ...
          </ExportEntries>
          <SummaryFields>
            <Field name=... id="2" repetition="2"
        table=.../>
            <Field name=... id="2" repetition="2"
        table=.../>
            ...
          </SummaryFields>
        </Step>
```
