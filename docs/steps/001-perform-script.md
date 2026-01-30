---
id: 1
name: "Perform Script"
category: Control
status: draft
input_patterns:
  - "Perform Script [ ... ]"
fm_name: "Perform Script"
xml:
  step_name: "Perform Script"
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

- `name="Perform Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="1"` for all `Perform Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Script parameters**: When a script parameter is specified (e.g., `Parameter: $variable` or `Parameter: calculation`):
  - Include a `<Calculation>` element as a direct child of `<Step>` containing the parameter expression, wrapped in `<![CDATA[ ... ]]>`.
  - Optionally include a `<DisplayCalculation>` element as a direct child of `<Step>` for display purposes (typically contains the same calculation).
  - The parameter calculation can be a variable reference (e.g., `$findSitelokParameter`), a literal value, or any valid FileMaker calculation expression.
- **"Specified: From list" limitation**: When the input contains `Specified: From list`, the XML conversion cannot reliably preserve the script name because this option requires database-specific value list references. **In this case, you must:**
  1. **Add a Comment step immediately before** the Perform Script step containing the original plain text for manual reference.
  2. Generate the Perform Script XML as best as possible (the script name may appear as `<unknown>` in FileMaker).
  3. The developer will need to manually correct the script reference in FileMaker using the comment as a guide.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{name}` - appears conditionally (for external scripts)
  - `{PathList}` - appears conditionally (for external scripts)
  - `<Calculation>` and `<DisplayCalculation>` for script parameters - appear only when a script parameter is specified

## Examples

### Example 1: Perform Script without parameter

**Input (plain text)**:
```plaintext
Perform Script [ "EndOfYear" ]
```

**Output (XML, step-only)**:
```xml
<Step enable="True" id="1" name="Perform Script">
  <Script name="EndOfYear" id="1"/>
</Step>
```

### Example 2: Perform Script with script parameter (variable)

**Input (plain text)**:
```plaintext
Perform Script [ "EndOfYear" ; Parameter: $findSitelokParameter ]
```

**Output (XML, step-only)**:
```xml
<Step enable="True" id="1" name="Perform Script">
  <Calculation>
    <![CDATA[$findSitelokParameter]]>
  </Calculation>
  <DisplayCalculation>
    <Calculation>
      <![CDATA[$findSitelokParameter]]>
    </Calculation>
  </DisplayCalculation>
  <Script name="EndOfYear" id="1"/>
</Step>
```

### Example 3: Perform Script with script parameter (calculation)

**Input (plain text)**:
```plaintext
Perform Script [ "EndOfYear" ; Parameter: Get ( ScriptParameter ) ]
```

**Output (XML, step-only)**:
```xml
<Step enable="True" id="1" name="Perform Script">
  <Calculation>
    <![CDATA[Get ( ScriptParameter )]]>
  </Calculation>
  <DisplayCalculation>
    <Calculation>
      <![CDATA[Get ( ScriptParameter )]]>
    </Calculation>
  </DisplayCalculation>
  <Script name="EndOfYear" id="1"/>
</Step>
```

### Example 4: Perform Script with calculated script name and parameter

**Input (plain text)**:
```plaintext
Perform Script [ Calculated: "Script name" ; Parameter: $findSitelokParameter ]
```

**Output (XML, step-only)**:
```xml
<Step enable="True" id="1" name="Perform Script">
          <Calculated>
           <Calculation>
              <![CDATA["Script name"]]>
           </Calculation>
          </Calculated>
  <Calculation>
    <![CDATA[$findSitelokParameter]]>
  </Calculation>
  <DisplayCalculation>
    <Calculation>
      <![CDATA[$findSitelokParameter]]>
    </Calculation>
  </DisplayCalculation>
</Step>
```

### Example 5: Perform Script with "Specified: From list" (requires manual correction)

**Input (plain text)**:
```plaintext
Perform Script [
  Specified: From list ;
  "CreateOrUpdateWWWRecord" ;
  Parameter: $createSheetParameter
]
```

**Output (XML, with comment for manual reference)**:
```xml
<Step enable="True" id="89" name="Comment">
  <Text>Original: Perform Script [ Specified: From list ; "CreateOrUpdateWWWRecord" ; Parameter: $createSheetParameter ]</Text>
</Step>
<Step enable="True" id="1" name="Perform Script">
  <Calculation>
    <![CDATA[$createSheetParameter]]>
  </Calculation>
           <DisplayCalculation>
           <Calculation>
      <![CDATA[$createSheetParameter]]>
           </Calculation>
  </DisplayCalculation>
  <!-- Note: Script name may appear as <unknown> in FileMaker. Use the comment above to manually correct. -->
        </Step>
```

**Important**: When FileMaker imports this XML, the script name will likely appear as `<unknown>`. The developer must:
1. Open the script in FileMaker
2. Use the comment step to see the original intent
3. Manually select the correct script from the value list in FileMaker's script step options
