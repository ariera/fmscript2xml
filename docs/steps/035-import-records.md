---
id: 35
name: "Import Records"
category: Records
status: draft
input_patterns:
  - "Import Records [ ... ]"
fm_name: "Import Records"
xml:
  step_name: "Import Records"
  enable_default: True
  wrapper: step-only
---

## Description

is only meaningful when method value is

          "UpdateOnMatch".



           contains a list of all fields in the destination table.

          Entries that are blank are represented by an empty field node .



           is only present if  is "XMLFile".



          {PathList} in  is the same as that in

          .
  is only present if  is "XMLHttp"
  is only present if  is "XMLCalculation"



           is only present if  is "XSLFile"



           is only present if  is "XSLHttp"



           is only present if  is "XSLCalculation"



           is only present if  is "Calculation"



           is only present if  is "Query"



          {PathList} can consist of multiple absolute or relative paths, the first valid

          one of which is used at execution time.
For a request to import into a new table : 

  element. is absent
 {FieldName} for each  element child of

 element is index of field from data source to import into that target field. Each target field's actual name will be determined by the name of the corresponding source field in the same position (as previously established in the 'Import Mapping' dialog) when the script step is eventually performed.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Import Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="35"` for all `Import Records` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Do not** include a `Table id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Table>` element specifies the target table.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{for Excel file data source (specified in <UniversalPathList>) :
          }` - appears conditionally
  - `{for non-Excel file data source (specified in <UniversalPathList>) :
          }` - appears conditionally
  - `{for folder data source (specified in <UniversalPathList>) :
          }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="35" name="Import Records">
            <NoInteract state="True"/>
            <NotWinStep state="True"/>
            <Restore state="True"/>
            <VerifySSLCertificates state="True"/>
            <DataSourceType value="File"/>
          ...
          ...
          ...
          ...
 ...</XMLFile>
              <XMLHttp>...</XMLHttp>
              <XMLCalc>
                <Calculation>
                  <![CDATA[CalcString]]>
                </Calculation>
              </XMLCalc>
              <XSLFile>
                <UniversalPathList>...</UniversalPathList>
              </XSLFile>
              <XSLHttp>...</XSLHttp>
              <XSLCalc>
                <Calculation>
                  <![CDATA[CalcString]]>
                </Calculation>
              </XSLCalc>
          }
          ...</Query>
          }
            <UniversalPathList>...</UniversalPathList>
            <ImportOptions method="UpdateOnMatch" SplitRepetitions="True"
          AutoEnter="True" AddRemainingRecords="True" MatchFieldNames="True"
               CharacterSet="Windows"/>
            <Table name=... id="1"/>
            <TargetFields>
              <Field name=... id="1" map="Import"/>
              <Field/>
              <Field name=... id="2" map="Match"/>
              ...
            </TargetFields>
          </Step>
```
