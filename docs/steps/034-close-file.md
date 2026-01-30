---
id: 34
name: "Close File"
category: Files
status: draft
input_patterns:
  - "Close File [ ... ]"
fm_name: "Close File"
xml:
  step_name: "Close File"
  enable_default: True
  wrapper: step-only
---

## Description

If neither  nor  nodes 

          are present, the current file is closed. 
{PathList} can consist of multiple absolute or relative paths, the first valid one of which is used at execution time.
  and  are present only if  is "False" (that is, the user has entered login credentials for the ODBC data source).

## Mapping rules

- `name="Close File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="34"` for all `Close File` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a FileMaker data source:
            <FileReference name={name}` - appears conditionally
  - `{PathList}` - appears conditionally
  - `{For an ODBC data source:
            <OdbcDataSource name={name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="34" name="Close File">
            ... id="1">
              <UniversalPathList>...</UniversalPathList>
            </FileReference>
            }
            ... id="1" DSN="..."
             promptForLogin="False">
              <Username>
                <Calculation>
                  <![CDATA[CalcString]]>
                </Calculation>
              </Username>
                <Calculation>
                  <![CDATA[CalcString]]>
                </Calculation>
              <FilterTables tableName="..."
               schemaName="..."
               catalogName="..."
               typeBasedFilter="True" retrieveTables="True"
               retrieveViews="True" retrieveSystemTables="True"/>
            </OdbcDataSource>
            }
          </Step>
```
