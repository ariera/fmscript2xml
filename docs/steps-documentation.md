# FileMaker Script Steps Documentation

Complete reference documentation for all FileMaker script steps and functions.
Use this documentation to convert plain text script steps into valid XML format.

---

## Table of Contents

1. [Script Steps by Category](#script-steps-by-category)
2. [FileMaker Functions](#filemaker-functions)
3. [Important Policies](#important-policies)

# Script Steps by Category

The following sections document all FileMaker script steps, organized by category.
Each step includes its ID, name, mapping rules, and XML examples.

**Total script steps documented: 167**

## Account (6 steps)

- **Step 83**: `Change Password` [draft]
- **Step 134**: `Add Account` [draft]
- **Step 135**: `Delete Account` [draft]
- **Step 136**: `Reset Account Password` [draft]
- **Step 137**: `Enable Account` [draft]
- **Step 138**: `Re-Login` [draft]

### Step 83: Change Password

**Status**: draft

## Description

FileMaker script step: Change Password

## Mapping rules

- `name="Change Password"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="83"` for all `Change Password` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="83" name="Change Password">
  
          
  <NoInteract state="True"/>
  
          
  <OldPassword>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </OldPassword>
  
          
  <NewPassword>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </NewPassword>
  
        
</Step>

```

---

### Step 134: Add Account

**Status**: draft

## Description

FileMaker script step: Add Account

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Add Account"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="134"` for all `Add Account` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="134" name="Add Account" enable="True">
          <ChgPwdOnNextLogin value="True">
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
        </Step>
```

---

### Step 135: Delete Account

**Status**: draft

## Description

FileMaker script step: Delete Account

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Delete Account"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="135"` for all `Delete Account` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="135" name="Delete Account" enable="True">
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
        </Step>
```

---

### Step 136: Reset Account Password

**Status**: draft

## Description

FileMaker script step: Reset Account Password

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Reset Account Password"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="136"` for all `Reset Account Password` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="136" name="Reset Account Password" enable="True">
          <ChgPwdOnNextLogin value="True">
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
        </Step>
```

---

### Step 137: Enable Account

**Status**: draft

## Description

FileMaker script step: Enable Account

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Enable Account"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="137"` for all `Enable Account` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="137" name="Enable Account" enable="True">
          <AccountOperation value="Activate"/>
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
        </Step>
```

---

### Step 138: Re-Login

**Status**: draft

## Description

FileMaker script step: Re-Login

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Re-Login"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="138"` for all `Re-Login` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<ScriptStep id="138" name="Re-Login" enable="True">
          <NoInteract state="True"/>
          <AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </AccountName>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
        </Step>
```

---

## Control (21 steps)

- **Step 1**: `Perform Script` [draft]
- **Step 62**: `Pause/Resume Script` [draft]
- **Step 68**: `If` [draft]
- **Step 69**: `Else` [draft]
- **Step 70**: `End If` [draft]
- **Step 71**: `Loop` [draft]
- **Step 72**: `Exit Loop If` [draft]
- **Step 73**: `End Loop` [draft]
- **Step 84**: `Set Layout Object Animation` [draft]
- **Step 85**: `Allow User Abort` [draft]
- **Step 86**: `Set Error Capture` [draft]
- **Step 90**: `Halt Script` [draft]
- **Step 103**: `Exit Script` [draft]
- **Step 125**: `Else If` [draft]
- **Step 141**: `Set Variable` [draft]
- **Step 145**: `Go to Object` [draft]
- **Step 146**: `Set Web Viewer` [draft]
- **Step 148**: `Install OnTimer Script` [draft]
- **Step 164**: `Perform Script on Server` [draft]
- **Step 185**: `Configure Region Monitor Script` (vnewto16) [draft]
- **Step 187**: `Configure Local Notification` (vnewto17) [draft]

### Step 1: Perform Script

**Status**: draft

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

---

### Step 62: Pause/Resume Script

**Status**: draft

## Description

node exists when  is "ForDuration".

## Mapping rules

- `name="Pause/Resume Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="62"` for all `Pause/Resume Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="62" name="Pause/Resume Script">
  
           
  <Calculation>
              120
           </Calculation>
  
        
</Step>

```

---

### Step 68: If

**Status**: draft

## Description

FileMaker script step: If

## Mapping rules

- `name="If"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="68"` for all `If` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="68" name="If">
  
           
  <Calculation>
              CalcString
           </Calculation>
  
        
</Step>

```

---

### Step 69: Else

**Status**: draft

## Description

FileMaker script step: Else

## Mapping rules

- `name="Else"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="69"` for all `Else` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="69" name="Else">
        </Step>

```

---

### Step 70: End If

**Status**: draft

## Description

FileMaker script step: End If

## Mapping rules

- `name="End If"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="70"` for all `End If` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="70" name="End If">
        </Step>

```

---

### Step 71: Loop

**Status**: draft

## Description

FileMaker script step: Loop

## Mapping rules

- `name="Loop"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="71"` for all `Loop` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="71" name="Loop">
        </Step>

```

---

### Step 72: Exit Loop If

**Status**: draft

## Description

FileMaker script step: Exit Loop If

## Mapping rules

- `name="Exit Loop If"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="72"` for all `Exit Loop If` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="72" name="Exit Loop If">
  
           
  <Calculation>
              CalcString
           </Calculation>
  
        
</Step>

```

---

### Step 73: End Loop

**Status**: draft

## Description

FileMaker script step: End Loop

## Mapping rules

- `name="End Loop"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="73"` for all `End Loop` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="73" name="End Loop">
        </Step>

```

---

### Step 84: Set Layout Object Animation

**Status**: draft

## Description

FileMaker script step: Set Layout Object Animation

## Mapping rules

- `name="Set Layout Object Animation"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="84"` for all `Set Layout Object Animation` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="true" id="84" name="Set Layout Object Animation">
           <Set state="true"|"false"/>
        </Step>
```

---

### Step 85: Allow User Abort

**Status**: draft

## Description

FileMaker script step: Allow User Abort

## Mapping rules

- `name="Allow User Abort"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="85"` for all `Allow User Abort` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="85" name="Allow User Abort">
  
          
  <Set state="True"/>
  
        
</Step>

```

---

### Step 86: Set Error Capture

**Status**: draft

## Description

FileMaker script step: Set Error Capture

## Mapping rules

- `name="Set Error Capture"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="86"` for all `Set Error Capture` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="86" name="Set Error Capture">
  
           
  <Set state="True"/>
  
        
</Step>

```

---

### Step 90: Halt Script

**Status**: draft

## Description

FileMaker script step: Halt Script

## Mapping rules

- `name="Halt Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="90"` for all `Halt Script` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="90" name="Halt Script">
        </Step>

```

---

### Step 103: Exit Script

**Status**: draft

## Description

FileMaker script step: Exit Script

## Mapping rules

- `name="Exit Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="103"` for all `Exit Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="103" name="Exit Script">
  
            
  <Calculation>
               CalcString
            </Calculation>
  
        
</Step>

```

---

### Step 125: Else If

**Status**: draft

## Description

FileMaker script step: Else If

## Mapping rules

- `name="Else If"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="125"` for all `Else If` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="125" name="Else If">
  
           
  <Calculation>CalcString</Calculation>
  
        
</Step>

```

---

### Step 141: Set Variable

**Status**: draft

## Description

FileMaker script step: Set Variable

## Mapping rules

- `name="Set Variable"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="141"` for all `Set Variable` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Variable name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="141" name="Set Variable">
  
            
  <Name>...</Name>
  
            
  <Value>
    
               
    <Calculation>
                CalcString
               </Calculation>
    
            
  </Value>
  
            
  <Repetition>
    
               
    <Calculation>
                CalcString
               </Calculation>
    
            
  </Repetition>
  
        
</Step>

```

---

### Step 145: Go to Object

**Status**: draft

## Description

FileMaker script step: Go to Object

## Mapping rules

- `name="Go to Object"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="145"` for all `Go to Object` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="145" name="Go to Object">
  
           
  <ObjectName>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </ObjectName>
  
           
  <Repetition>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 146: Set Web Viewer

**Status**: draft

## Description

element is present when 

         is "GoToURL."

## Mapping rules

- `name="Set Web Viewer"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="146"` for all `Set Web Viewer` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="146" name="Set Web Viewer">
  
           
  <Action value="Reset"/>
  
           
  <ObjectName>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </ObjectName>
  
           
  <URL custom="True">
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </URL>
  
        
</Step>

```

---

### Step 148: Install OnTimer Script

**Status**: draft

## Description

FileMaker script step: Install OnTimer Script

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Install OnTimer Script"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="148"` for all `Install OnTimer Script` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="148" name="Install OnTimer Script">
  
 
  <Interval>
    
          
    <Calculation>
          CalcString
          </Calculation>
    
          
  </Interval>
  

  <Script id="1" name="Script Name "/>
  

</Step>

```

---

### Step 164: Perform Script on Server

**Status**: draft

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

---

### Step 185: Configure Region Monitor Script

**Version**: newto16

**Status**: draft

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

---

### Step 187: Configure Local Notification

**Version**: newto17

**Status**: draft

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

---

## Editing (8 steps)

- **Step 45**: `Undo/Redo` [draft]
- **Step 46**: `Cut` [draft]
- **Step 47**: `Copy` [draft]
- **Step 48**: `Paste` [draft]
- **Step 49**: `Clear` [draft]
- **Step 50**: `Select All` [draft]
- **Step 128**: `Perform Find/Replace` [draft]
- **Step 130**: `Set Selection` [draft]

### Step 45: Undo/Redo

**Status**: draft

## Description

FileMaker script step: Undo/Redo

## Mapping rules

- `name="Undo/Redo"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="45"` for all `Undo/Redo` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="45" name="Undo/Redo">
  
          
  <UndoRedo value="Toggle"/>
  
        
</Step>

```

---

### Step 46: Cut

**Status**: draft

## Description

FileMaker script step: Cut

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Cut"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="46"` for all `Cut` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="46" name="Cut">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 47: Copy

**Status**: draft

## Description

FileMaker script step: Copy

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Copy"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="47"` for all `Copy` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="47" name="Copy">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 48: Paste

**Status**: draft

## Description

FileMaker script step: Paste

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Paste"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="48"` for all `Paste` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="48" name="Paste">
  
          
  <NoStyle state="True"/>
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 49: Clear

**Status**: draft

## Description

FileMaker script step: Clear

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Clear"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="49"` for all `Clear` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="49" name="Clear">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f4" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 50: Select All

**Status**: draft

## Description

FileMaker script step: Select All

## Mapping rules

- `name="Select All"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="50"` for all `Select All` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="50" name="Select All">
        </Step>

```

---

### Step 128: Perform Find/Replace

**Status**: draft

## Description

FileMaker script step: Perform Find/Replace

## Mapping rules

- `name="Perform Find/Replace"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="128"` for all `Perform Find/Replace` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="128" name="Perform Find/Replace">
  
          
  <NoInteract state="True"/>
  
          
  <FindReplaceOperation type="FindNext" direction="Forward" MatchCase="False" MatchWholeWords="False" AcrossOptions="All" WithinOptions="All"/>
  
          
  <FindCalc>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </FindCalc>
  
          
  <ReplaceCalc>
    
            
    <Calculation>
              ...
            </Calculation>
    
          
  </ReplaceCalc>
  
        
</Step>

```

---

### Step 130: Set Selection

**Status**: draft

## Description

FileMaker script step: Set Selection

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Set Selection"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="130"` for all `Set Selection` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally
  - `{FieldName}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="130" name="Set Selection">
          <StartPosition>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </StartPosition>
          <EndPosition>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </EndPosition>
          <Field name=... id="2" table=.../>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
```

---

## Fields (21 steps)

- **Step 11**: `Insert from Index` [draft]
- **Step 12**: `Insert from Last Visited` [draft]
- **Step 13**: `Insert Current Date` [draft]
- **Step 14**: `Insert Current Time` [draft]
- **Step 40**: `Relookup Field Contents` [draft]
- **Step 56**: `Insert Picture` [draft]
- **Step 60**: `Insert Current User Name` [draft]
- **Step 61**: `Insert Text` [draft]
- **Step 76**: `Set Field` [draft]
- **Step 77**: `Insert Calculated Result` [draft]
- **Step 78**: `#[OBSOLETE]Insert Object` [draft]
- **Step 91**: `Replace Field Contents` [draft]
- **Step 96**: `#[OBSOLETE]Update Link` [draft]
- **Step 116**: `Set Next Serial Value` [draft]
- **Step 131**: `Insert File` [draft]
- **Step 132**: `Export Field Contents` [draft]
- **Step 147**: `Set Field By Name` [draft]
- **Step 158**: `Insert PDF` [draft]
- **Step 159**: `Insert Audio/Video` [draft]
- **Step 160**: `Insert from URL` [draft]
- **Step 161**: `Insert from Device` [draft]

### Step 11: Insert from Index

**Status**: draft

## Description

FileMaker script step: Insert from Index

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert from Index"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="11"` for all `Insert from Index` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="11" name="Insert from Index">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 12: Insert from Last Visited

**Status**: draft

## Description

FileMaker script step: Insert from Last Visited

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert from Last Visited"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="12"` for all `Insert from Last Visited` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="12" name="Insert from Last Visited">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 13: Insert Current Date

**Status**: draft

## Description

FileMaker script step: Insert Current Date

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Current Date"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="13"` for all `Insert Current Date` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f3" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="13" name="Insert Current Date">
  
          
  <SelectAll state="True"/>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 14: Insert Current Time

**Status**: draft

## Description

FileMaker script step: Insert Current Time

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Current Time"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="14"` for all `Insert Current Time` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f4" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="14" name="Insert Current Time">
  
          
  <SelectAll state="True"/>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 40: Relookup Field Contents

**Status**: draft

## Description

FileMaker script step: Relookup Field Contents

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Relookup Field Contents"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="40"` for all `Relookup Field Contents` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="40" name="Relookup Field Contents">
  
          
  <NoInteract state="True"/>
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 56: Insert Picture

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Insert Picture"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="56"` for all `Insert Picture` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="56" name="Insert Picture">
  
          
  <UniversalPathList type="Reference">...</UniversalPathList>
  
        
</Step>

```

---

### Step 60: Insert Current User Name

**Status**: draft

## Description

FileMaker script step: Insert Current User Name

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Current User Name"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="60"` for all `Insert Current User Name` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f4" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="60" name="Insert Current User Name">
  
          
  <SelectAll state="True"/>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 61: Insert Text

**Status**: draft

## Description

FileMaker script step: Insert Text

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Text"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="61"` for all `Insert Text` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f1" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="61" name="Insert Text">
  
          
  <SelectAll state="True"/>
  
          
  <Text>&quot;Text to insert&quot;</Text>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 76: Set Field

**Status**: draft

## Description

FileMaker script step: Set Field

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Set Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="76"` for all `Set Field` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="76" name="Set Field">
  
          
  <Field name="f1" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 77: Insert Calculated Result

**Status**: draft

## Description

FileMaker script step: Insert Calculated Result

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert Calculated Result"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="77"` for all `Insert Calculated Result` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
         <Field table="f3" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="77" name="Insert Calculated Result">
  
          
  <SelectAll state="True"/>
  
           
  <Calculation>
              CalcString
           </Calculation>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 78: #[OBSOLETE]Insert Object

**Status**: draft

## Description

is only present if the inserted object is of type "Create

          from File".


Note : Although it makes sense for the 

           attribute to be supported for this script

          step, the setting of the 'Link' checkbox in the Insert Object dialog is

          actually stored in the OLEData element's CDATA, despite the fact that the file

          chosen via this dialog is not (since it is stored in the

           element).
It is no longer possible to create this script; although, you can have step in a converted file.

## Mapping rules

- `name="#[OBSOLETE]Insert Object"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="78"` for all `#[OBSOLETE]Insert Object` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally
  - `{OLE data}` - appears conditionally
  - `{Object Type}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="78" name="#[OBSOLETE]Insert Object">
  
          
  <Set state="True"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
          
  <OLEData>
            ...
          </OLEData>
  
          
  <ObjectType>...</ObjectType>
  
        
</Step>

```

---

### Step 91: Replace Field Contents

**Status**: draft

## Description

reflects the user's choice of what to replace the specified

          fields contents with.
  is present when

           is "SerialNumbers".
  and  can

          optionally be used to control serial number generation.
  is present when  is "Calculation".

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Replace Field Contents"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="91"` for all `Replace Field Contents` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="None">
        </Step>
        <Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="CurrentContents">
          <Field name="f3" id="2" table="test"/>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="SerialNumbers">
          <SerialNumbers UseEntryOptions="False"
            InitialValue="0" Increment="1"
        UpdateEntryOptions="False"/>
          <Field name="f3" id="2" table="test"/>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
        <Step enable="True" id="91" name="Replace Field Contents">
          <NoInteract state="True"/>
          <With value="Calculation">
          <Calculation>
            <![CDATA[Abs ( f3 )]]>
          </Calculation>
          <Field name="f3" id="2" table="test"/>
          <Repetition>
             <Calculation>
               <![CDATA["Value"]]>
             </Calculation>
           </Repetition>
        </Step>
```

---

### Step 96: #[OBSOLETE]Update Link

**Status**: draft

## Description

It is no longer possible to create this script; although, you can have step in a converted file.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="#[OBSOLETE]Update Link"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="96"` for all `#[OBSOLETE]Update Link` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="96" name="#[OBSOLETE]Update Link">
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 116: Set Next Serial Value

**Status**: draft

## Description

FileMaker script step: Set Next Serial Value

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Set Next Serial Value"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="116"` for all `Set Next Serial Value` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="116" name="Set Next Serial Value">
  
          
  <Calculation>
            12
          </Calculation>
  
          
  <Field name="f3" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 131: Insert File

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="131"` for all `Insert File` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally
  - `{For a field as the target:
         <Field table="f4" id="2" name="test"/>
         }` - appears conditionally
  - `{For a variable as the target:
         <Field>$VariableName</Field>
         }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="131" name="Insert File">
  
          
  <UniversalPathList type="Reference">...</UniversalPathList>
  
         ...
 ...
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
  <DialogOptions asFile="True" enable="True">
    
        
    <Storage type="UserChoice"/>
    
        
    <Compress type="UserChoice"/>
    					
    <FilterList>
      
        
      <Filter id="0">
        
        
        <name>
          
        
          <Calculation>&quot;All Files&quot;</Calculation>
          
        
        </name>
        
        *.*
        
      </Filter>
      
        
    </FilterList>
  </DialogOptions>
  
        
</Step>

```

---

### Step 132: Export Field Contents

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Export Field Contents"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="132"` for all `Export Field Contents` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="132" name="Export Field Contents">
  
          
  <AutoOpen state="True"/>
  
          
  <CreateEmail state="True"/>
  
          
  <CreateDirectories state="True"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
          
  <Field name="FieldName" id="2" table="TableName"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 147: Set Field By Name

**Status**: draft

## Description

specifies the target field's name
 specifies the value to be placed in that field.

## Mapping rules

- `name="Set Field By Name"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="147"` for all `Set Field By Name` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="147" name="Set Field By Name">
  

  <TargetName>
    
          
    <Calculation>
          CalcString
          </Calculation>
    
          
  </TargetName>
  
 
  <Result>
    
             
    <Calculation>
                  CalcString
             </Calculation>
    
          
  </Result>
  

</Step>

```

---

### Step 158: Insert PDF

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Insert PDF"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="158"` for all `Insert PDF` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="158" name="Insert PDF">
  
            
  <UniversalPathList type="Reference">...</UniversalPathList>
  
        
</Step>

```

---

### Step 159: Insert Audio/Video

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Insert Audio/Video"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="159"` for all `Insert Audio/Video` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="159" name="Insert Audio/Video">
  
            
  <UniversalPathList type="Reference">...</UniversalPathList>
  
        
</Step>

```

---

### Step 160: Insert from URL

**Status**: draft

## Description

FileMaker script step: Insert from URL

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Insert from URL"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="160"` for all `Insert from URL` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{For a field as the target:
            <Field table="f3" id="2" name="test"/>
            }` - appears conditionally
  - `{For a variable as the target:
            <Field>$VariableName</Field>
            }` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="160" name="Insert from URL">
  
            
  <NoInteract state="True"/>
  
            
  <SelectAll state="True"/>
  
            
  <VerifySSLCertificates state="True"/>
  
  
  <DontEncodeURL state="False"/>
  
            
  <Calculation>
               &quot;Value&quot;
            </Calculation>
  
            ...
             ...
            
  <CURLOptions>
    
             
    <Calculation>&quot;Value&quot;</Calculation>
    
            
  </CURLOptions>
  

</Step>

```

---

### Step 161: Insert from Device

**Status**: draft

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

---

## Files (8 steps)

- **Step 33**: `Open File` [draft]
- **Step 34**: `Close File` [draft]
- **Step 37**: `Save a Copy as` [draft]
- **Step 82**: `New File` [draft]
- **Step 84**: `Set Multi-User` [draft]
- **Step 94**: `Set Use System Formats` [draft]
- **Step 95**: `Recover File` [draft]
- **Step 139**: `Convert File` [draft]

### Step 33: Open File

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid one of which is used at execution time.
  and  are present only if  is "False" (that is, user has entered login credentials for the ODBC data source).

## Mapping rules

- `name="Open File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="33"` for all `Open File` steps.
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
<Step enable="True" id="33" name="Open File">
            <Option state="True"/>
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
               typeBasedFilter="True"  retrieveTables="True"
               retrieveViews="True" retrieveSystemTables="True"/>
            </OdbcDataSource>
            }
          </Step>
```

---

### Step 34: Close File

**Status**: draft

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

---

### Step 37: Save a Copy as

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Save a Copy as"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="37"` for all `Save a Copy as` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="37" name="Save a Copy as">
  
          
  <AutoOpen state="True"/>
  
          
  <CreateEmail state="True"/>
  
          
  <CreateDirectories state="True"/>
  
          
  <SaveAsType value="Copy"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
        
</Step>

```

---

### Step 82: New File

**Status**: draft

## Description

FileMaker script step: New File

## Mapping rules

- `name="New File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="82"` for all `New File` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="82" name="New File">
        </Step>

```

---

### Step 84: Set Multi-User

**Status**: draft

## Description

FileMaker script step: Set Multi-User

## Mapping rules

- `name="Set Multi-User"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="84"` for all `Set Multi-User` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="84" name="Set Multi-User">
  
          
  <MultiUser value="True"/>
  
        
</Step>

```

---

### Step 94: Set Use System Formats

**Status**: draft

## Description

FileMaker script step: Set Use System Formats

## Mapping rules

- `name="Set Use System Formats"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="94"` for all `Set Use System Formats` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="94" name="Set Use System Formats">
  
          
  <Set state="True"/>
  
        
</Step>

```

---

### Step 95: Recover File

**Status**: draft

## Description

{PathList} can consist of multiple absolute or relative paths, the first valid

        one of which is used at execution time.

## Mapping rules

- `name="Recover File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="95"` for all `Recover File` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="95" name="Recover File">
  
          
  <NoInteract state="True"/>
  
          
  <UniversalPathList>...</UniversalPathList>
  
        
</Step>

```

---

### Step 139: Convert File

**Status**: draft

## Description

FileMaker script step: Convert File

## Mapping rules

- `name="Convert File"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="139"` for all `Convert File` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Import Records, except for folder data source options,
           which Convert File does not have.}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="139" name="Convert File">
          ...
        </Step>

```

---

## Found Sets (13 steps)

- **Step 21**: `Unsort Records` [draft]
- **Step 23**: `Show All Records` [draft]
- **Step 24**: `Modify Last Find` [draft]
- **Step 25**: `Omit Record` [draft]
- **Step 26**: `Omit Multiple Records` [draft]
- **Step 27**: `Show Omitted Only` [draft]
- **Step 28**: `Perform Find` [draft]
- **Step 39**: `Sort Records` [draft]
- **Step 126**: `Constrain Found Set` [draft]
- **Step 127**: `Extend Found Set` [draft]
- **Step 150**: `Perform Quick Find` [draft]
- **Step 154**: `Sort Records by Field` [draft]
- **Step 155**: `Find Matching Records` [draft]

### Step 21: Unsort Records

**Status**: draft

## Description

FileMaker script step: Unsort Records

## Mapping rules

- `name="Unsort Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="21"` for all `Unsort Records` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="21" name="Unsort Records">
        </Step>

```

---

### Step 23: Show All Records

**Status**: draft

## Description

FileMaker script step: Show All Records

## Mapping rules

- `name="Show All Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="23"` for all `Show All Records` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="23" name="Show All Records">
        </Step>

```

---

### Step 24: Modify Last Find

**Status**: draft

## Description

FileMaker script step: Modify Last Find

## Mapping rules

- `name="Modify Last Find"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="24"` for all `Modify Last Find` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="24" name="Modify Last Find">
        </Step>

```

---

### Step 25: Omit Record

**Status**: draft

## Description

FileMaker script step: Omit Record

## Mapping rules

- `name="Omit Record"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="25"` for all `Omit Record` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="25" name="Omit Record">
        </Step>

```

---

### Step 26: Omit Multiple Records

**Status**: draft

## Description

FileMaker script step: Omit Multiple Records

## Mapping rules

- `name="Omit Multiple Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="26"` for all `Omit Multiple Records` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="26" name="Omit Multiple Records">
  
          
  <NoInteract state="True"/>
  
            
  <Calculation>
              CalcString
            </Calculation>
  
        
</Step>

```

---

### Step 27: Show Omitted Only

**Status**: draft

## Description

FileMaker script step: Show Omitted Only

## Mapping rules

- `name="Show Omitted Only"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="27"` for all `Show Omitted Only` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="27" name="Show Omitted Only">
        </Step>

```

---

### Step 28: Perform Find

**Status**: draft

## Description

Query node can have 1 or more RequestRow sub-nodes.
Each RequestRow node can in turn have 1 or more Criteria sub-nodes.
  contains the actual criteria itself that will be applied to

          . 
  is only output if > 1.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Perform Find"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="28"` for all `Perform Find` steps.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="28" name="Perform Find">
  
          
  <Restore state="True"/>
  
          
  <Query table="test123">
    
            
    <RequestRow operation="Include">
      
              
      <Criteria>
        
                
        <Text>&gt; 11</Text>
        
                
        <Field name="f2" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
              
      <Criteria>
        
                
        <Text>&lt; 23</Text>
        
                
        <Field name="f3" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
            
    </RequestRow>
    
            
    <RequestRow operation="Exclude">
      
              
      <Criteria>
        
                
        <Text>&gt;
        &quot;wow&quot;</Text>
        
                
        <Field name="f3" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
              
      <Criteria>
        
                
        <Text>&gt;
        test</Text>
        
                
        <Field name="f4" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
              
      <Criteria>
        
                
        <Text>&gt; &quot;hello
        there </Text>
        
                
        <Field name="f5" id="2" repetition="2" table="test123"/>
        
              
      </Criteria>
      
            
    </RequestRow>
    
          
  </Query>
  
        
</Step>

```

---

### Step 39: Sort Records

**Status**: draft

## Description

node exists if  is Custom
  and  sub-nodes are optional.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Sort Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="39"` for all `Sort Records` steps.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="39" name="Sort Records">
  
          
  <NoInteract state="False"/>
  
          
  <Restore state="True"/>
  
          
  <SortList>
    
            
    <Sort type="Descending">
      
                
      <Field name="f1" id="1" table="test123"/>
      
            
    </Sort>
    
            
    <Sort type="Ascending">
      
                
      <Field name="f4" id="2" table="test123"/>
      
              
      <SummaryField>
        
                
        <Field name="summary" id="3" table="test123"/>
        
              
      </SummaryField>
      
              
      <OverrideLanguage language="Japanese"/>
      
            
    </Sort>
    
            
    <Sort type="Custom">
      
                
      <Field name="f5" id="4" table="test123"/>
      
              
      <ValueList name="New Value List" id="1"/>
      
            
    </Sort>
    
          
  </SortList>
  
        
</Step>

```

---

### Step 126: Constrain Found Set

**Status**: draft

## Description

{See Perform Find}

## Mapping rules

- `name="Constrain Found Set"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="126"` for all `Constrain Found Set` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Perform Find}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="126" name="Constrain Found Set">
           ...
        </Step>

```

---

### Step 127: Extend Found Set

**Status**: draft

## Description

{See Perform Find}

## Mapping rules

- `name="Extend Found Set"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="127"` for all `Extend Found Set` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Perform Find}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="127" name="Extend Found Set">
           ...
        </Step>

```

---

### Step 150: Perform Quick Find

**Status**: draft

## Description

FileMaker script step: Perform Quick Find

## Mapping rules

- `name="Perform Quick Find"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="150"` for all `Perform Quick Find` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="150" name="Perform Quick Find">
          <Calculation>
            <! [CDATA[ "Value" ]] >
          </Calculation>
        </Step>
```

---

### Step 154: Sort Records by Field

**Status**: draft

## Description

FileMaker script step: Sort Records by Field

## Mapping rules

- `name="Sort Records by Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="154"` for all `Sort Records by Field` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="154" name="Sort Records by Field">
  
        
  <SortRecordsByField value="SortAscending"/>
  
        
</Step>

```

---

### Step 155: Find Matching Records

**Status**: draft

## Description

FileMaker script step: Find Matching Records

## Mapping rules

- `name="Find Matching Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="155"` for all `Find Matching Records` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="155" name="Find Matching Records">
  
        
  <FindMatchingRecordsByField value="FindMatchingReplace"/>
  
        
</Step>

```

---

## Miscellaneous (21 steps)

- **Step 44**: `Exit Application` [draft]
- **Step 57**: `Send event` [draft]
- **Step 63**: `Send Mail` [draft]
- **Step 64**: `Send DDE Execute` [draft]
- **Step 65**: `Dial Phone` [draft]
- **Step 66**: `Speak` [draft]
- **Step 67**: `Perform AppleScript` [draft]
- **Step 87**: `Show Custom Dialog` [draft]
- **Step 89**: `Comment` [draft]
- **Step 93**: `Beep` [draft]
- **Step 102**: `Flush Cache to Disk` [draft]
- **Step 111**: `Open URL` [draft]
- **Step 115**: `Allow Toolbars` [draft]
- **Step 117**: `Execute SQL` [draft]
- **Step 142**: `Install Menu Set` [draft]
- **Step 167**: `Refresh Object` [draft]
- **Step 173**: `Get Directory` [draft]
- **Step 177**: `AVPlayer Play` [draft]
- **Step 178**: `AVPlayer Set Playback State` [draft]
- **Step 179**: `AVPlayer Set Options` [draft]
- **Step 180**: `Refresh Portal` [draft]

### Step 44: Exit Application

**Status**: draft

## Description

FileMaker script step: Exit Application

## Mapping rules

- `name="Exit Application"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="44"` for all `Exit Application` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="44" name="Exit Application">
        </Step>

```

---

### Step 57: Send event

**Status**: draft

## Description

is present when  is "File",

           is present when it is "Calculation", and  is

          present when it is "Text".
{PathList} can consist of multiple absolute or relative paths, the first valid

          one of which is used at execution time.

## Mapping rules

- `name="Send event"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="57"` for all `Send event` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally
  - `{CalcString}` - appears conditionally
  - `{TextString}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="57" name="Send event">
          <ContentType value="Calculation">
          <UniversalPathList>...</UniversalPathList>
          <Calculation>...</Calculation>
          <Text>...</Text>
          <Event class=... id=...
             TargetName=... TargetType=...
             BringTargetToForeground="True"
        WaitForCompletion="True"
             CopyResultToClipBoard="False"/>
        </Step>
```

---

### Step 63: Send Mail

**Status**: draft

## Description

FileMaker script step: Send Mail

## Mapping rules

- `name="Send Mail"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="63"` for all `Send Mail` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="63" name="Send Mail">
            <NoInteract state="True"/>
            <Attachment>
               <UniversalPathList>...</UniversalPathList>
            </Attachment>
   <To UseFoundSet="True">
               <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
            </To>
   <Cc UseFoundSet="True">
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </Cc>
   <Bcc UseFoundSet="True">
               <Calculation>
                 <![CDATA[<Step enable="True" id="63" name="Send Mail">
               </Calculation>
            </Bcc>
   <Subject>
               <Calculation>
                 <![CDATA["Subject"]]>
              </Calculation>
            </Subject>
   <Message>
               <Calculation>
                 <![CDATA["Message"]]>
               </Calculation>
            </Message>
  <SMTPNameDescription>
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPNameDescription>
   <SMTPEmailAddress >
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPEmailAddress>
   <SMTPReplyAddress >
              <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
           </SMTPReplyAddress>
   <SMTPServer>
              <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPServer>
   <SMTPPort >
               <Calculation>
                 <![CDATA[CalcString]]>
               </Calculation>
            </SMTPPort>
   <SMTPUserName>
                <Calculation>
                  <![CDATA[CalcString]]>
               </Calculation>
            </SMTPUserName>
   <SMTPPassword >
               <Calculation>
                 <![CDATA[CalcString]]>
              </Calculation>
            </SMTPPassword>
   <MultipleEmails state="True"/>
            <SendViaSMTP state ="True"/>
            <SMTPEncryptionType type="encryptionVal">
            <SMTPAuthenticationType type = "SMTPAuthenticationPlain"/>
          </Step>
```

---

### Step 64: Send DDE Execute

**Status**: draft

## Description

is present when  is "File"

          and  is present when it is "Calculation".
{PathList} can consist of multiple absolute or relative paths, the first valid

          one of which is used at execution time.

## Mapping rules

- `name="Send DDE Execute"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="64"` for all `Send DDE Execute` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="64" name="Send DDE Execute">
          <ContentType value="Calculation">
          <UniversalPathList>...</UniversalPathList>
          <ServiceName>
            <Calculation>
              <![CDATA["Word"]]>
            </Calculation>
          </ServiceName>
          <Topic>
            <Calculation>
              <![CDATA["TopicText"]]>
            </Calculation>
          </Topic>
          <Command>
            <Calculation>
              <![CDATA["Delete All"]]>
            </Calculation>
          </Command>
        </Step>
```

---

### Step 65: Dial Phone

**Status**: draft

## Description

FileMaker script step: Dial Phone

## Mapping rules

- `name="Dial Phone"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="65"` for all `Dial Phone` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="65" name="Dial Phone">
  
          
  <NoInteract state="True"/>
  
          
  <UseDialPreferences value="True"/>
  
          
  <Calculation>
            613-667-5030
          </Calculation>
  
        
</Step>

```

---

### Step 66: Speak

**Status**: draft

## Description

is only generated on the Mac and contains redundant information that only

        serves to make DDR reports (in particular HTML ones) more readable.

## Mapping rules

- `name="Speak"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="66"` for all `Speak` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{voice creator}` - appears conditionally
  - `{voice
        id}` - appears conditionally
  - `{voice name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="66" name="Speak">
           <SpeechOptions VoiceCreator=... VoiceId=...
              VoiceName=...
        WaitForCompletion="True"/>
           <Calculation>
             <![CDATA[CalcString]]>
           </Calculation>
        </Step>
```

---

### Step 67: Perform AppleScript

**Status**: draft

## Description

is present when  is "Calculation"

        and  is present when it is "Text".

## Mapping rules

- `name="Perform AppleScript"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="67"` for all `Perform AppleScript` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{compiled apple script data}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="67" name="Perform AppleScript">
          <ContentType value="Calculation">
          <CompiledScript>
            <![CDATA[...]]>
          </CompiledScript>
          <Calculation>
            <![CDATA["this is a calculated string"]]>
          </Calculation>
          <Text>This is a string literal</Text>
        </Step>
```

---

### Step 87: Show Custom Dialog

**Status**: draft

## Description

is only output if > 1

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Show Custom Dialog"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="87"` for all `Show Custom Dialog` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{CalcString}` - appears conditionally
  - `{CalcString}` - appears conditionally
  - `{For a field as the target:
              <Field name={FieldName}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="87" name="Show Custom Dialog">
          <Title>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </Title>
          <Message>
            <Calculation>
              <![CDATA[...]]>
            </Calculation>
          </Message>
  <Buttons>
              <Button CommitState="True">
                 <Calculation>
                   <![CDATA["OK"]]>
                 </Calculation>
              </Button>
              <Button CommitState="False">
                 <Calculation>
                   <![CDATA["Cancel"]]>
                 </Calculation>
              </Button>
              <Button CommitState="False">
                 <Calculation>
                   <![CDATA[Get( CurrentTime )]]>
                 </Calculation>
              </Button>
            </Buttons>
          <InputFields>
            <InputField
        UsePasswordCharacter="True">
              ... id="2" repetition="2" table=.../>
              }
              ...
              <Label>
                <Calculation>
                <![CDATA[...]]>
                </Calculation>
              </Label>
            <InputField>
            ...
            </InputField>
            ...
          </InputFields>
        </Step>
```

---

### Step 89: Comment

**Status**: draft

## Description

FileMaker script step: Comment

## Mapping rules

- `name="Comment"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="89"` for all `Comment` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="89" name="Comment">
  
          
  <Text>This is a comment</Text>
  
        
</Step>

```

---

### Step 93: Beep

**Status**: draft

## Description

FileMaker script step: Beep

## Mapping rules

- `name="Beep"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="93"` for all `Beep` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="93" name="Beep">
        </Step>

```

---

### Step 102: Flush Cache to Disk

**Status**: draft

## Description

FileMaker script step: Flush Cache to Disk

## Mapping rules

- `name="Flush Cache to Disk"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="102"` for all `Flush Cache to Disk` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="102" name="Flush Cache to Disk">
        </Step>

```

---

### Step 111: Open URL

**Status**: draft

## Description

FileMaker script step: Open URL

## Mapping rules

- `name="Open URL"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="111"` for all `Open URL` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="111" name="Open URL">
  
          
  <NoInteract state="True"/>
  
          
  <Calculation>
            &quot;https://www.filemaker.com&quot;
          </Calculation>
  
        
</Step>

```

---

### Step 115: Allow Toolbars

**Status**: draft

## Description

FileMaker script step: Allow Toolbars

## Mapping rules

- `name="Allow Toolbars"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="115"` for all `Allow Toolbars` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="115" name="Allow Toolbars">
  
          
  <Set state="True"/>
  
        
</Step>

```

---

### Step 117: Execute SQL

**Status**: draft

## Description

{See ODBC data source profile element in Import Records step}

## Mapping rules

- `name="Execute SQL"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="117"` for all `Execute SQL` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See ODBC data source profile element in Import Records step}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="117" name="Execute SQL">
  
          
  <NoInteract state="True"/>
  
          ...
        
</Step>

```

---

### Step 142: Install Menu Set

**Status**: draft

## Description

FileMaker script step: Install Menu Set

## Mapping rules

- `name="Install Menu Set"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="142"` for all `Install Menu Set` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Menu set name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="142" name="Install Menu Set">
           <UseAsFileDefault state="True"/>
           <CustomMenuSet id="3" name=.../>
        </Step>
```

---

### Step 167: Refresh Object

**Status**: draft

## Description

FileMaker script step: Refresh Object

## Mapping rules

- `name="Refresh Object"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="167"` for all `Refresh Object` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="167" name="Refresh Object">
  
           
  <ObjectName>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </ObjectName>
  
           
  <Repetition>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 173: Get Directory

**Status**: draft

## Description

FileMaker script step: Get Directory

## Mapping rules

- `name="Get Directory"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="173"` for all `Get Directory` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Variable name}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="173" name="Get Directory">
  
             
  <AllowFolderCreation state="True"/>
  

  <Name>...</Name>
  

  <DialogTitle>
    
            
    <Calculation>
          CalcString
          </Calculation>
    
          
  </DialogTitle>
  

  <DefaultLocation>
    
          
    <Calculation>
          CalcString
          </Calculation>
    
          
  </DefaultLocation>
  
         
</Step>

```

---

### Step 177: AVPlayer Play

**Status**: draft

## Description

The AVPlayer script step is used to initiate the playing of media from a field (must be a container), a layout object (must be a container), URL, or the active object (must be a container). When creating the script step, a field chooser, object chooser, or URL text entry box will be shown as appropriate. All parameters are optional. Only one of the "Field", "Object", or "URL" parameters may be specified for a given step. Playback of the active object is initiated if layout object is specified and no layout object name is provided.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="AVPlayer Play"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="177"` for all `AVPlayer Play` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Script step text}` - appears conditionally
  - `{Table}` - appears conditionally
  - `{FieldName}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="177" name="AVPlayer Play">
          <Source value="Object">
            <Calculation><![CDATA["ObjectName"]]></Calculation>
          </Source>
          <Repetition>
            <Calculation><![CDATA[3]]></Calculation>
          </Repetition>
          <Source value="Field">
          <Field table=... name=... repetition="1" id="2" />
          </Source>
          <Source value="URL">
            <Calculation><![CDATA["MyURL"]]></Calculation>
          </Source>
          <HideControls value="True"/>
          <DisableInteraction value="True"/>
            <Calculation><![CDATA[30]]></Calculation>
          <StartOffset>
            <Calculation><![CDATA[20]]></Calculation>
          </StartOffset>
          <EndOffset>
            <Calculation><![CDATA[120]]></Calculation>
          </EndOffset>
        </Step>
```

---

### Step 178: AVPlayer Set Playback State

**Status**: draft

## Description

Causes the AVPlayer to pause, resume playing, or stop. Once a player is stopped, it cannot be set to Playing (because "stopped" gives FileMaker permission to get rid of the AVPlayer). Conversely, this step will not work unless the AVPlayer was already either playing or paused.

## Mapping rules

- `name="AVPlayer Set Playback State"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="178"` for all `AVPlayer Set Playback State` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Script step text}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="178" name="AVPlayer Set Playback State">
           </StepText>
        </Step>
```

---

### Step 179: AVPlayer Set Options

**Status**: draft

## Description

All parameters are optional. This step is used to adjust the settings of a player that is either playing or paused. The parameters that are the same as in AVPlayer Play have the same meaning as in that step.

## Mapping rules

- `name="AVPlayer Set Options"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="179"` for all `AVPlayer Set Options` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Script step text}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="179" name="AVPlayer Set Options">
  
           value=&quot;Start Full Screen&quot;
          
  <HideControls value="True"/>
  
          
  <DisableExternalControls value="True"/>
  
          
  <DisableInteraction value="True"/>
  
            
  <Calculation>30</Calculation>
  
          
  <StartOffset>
    
            
    <Calculation>20</Calculation>
    
          
  </StartOffset>
  
          
  <EndOffset>
    
            
    <Calculation>120</Calculation>
    
          
  </EndOffset>
  
          
  <Volume>
    
            
    <Calculation>.5</Calculation>
    
          
  </Volume>
  
          
  <Zoom value="Fit"/>
  
          
  <Sequence value="Previous"/>
  
        
</Step>

```

---

### Step 180: Refresh Portal

**Status**: draft

## Description

FileMaker script step: Refresh Portal

## Mapping rules

- `name="Refresh Portal"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="180"` for all `Refresh Portal` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="180" name="Refresh Portal">
  
           
  <ObjectName>
    
              
    <Calculation>
                CalcString
              </Calculation>
    
           
  </ObjectName>
  
        
</Step>

```

---

## Navigation (12 steps)

- **Step 4**: `Go to Next Field` [draft]
- **Step 5**: `Go to Previous Field` [draft]
- **Step 6**: `Go to Layout` [draft]
- **Step 16**: `Go to Record/Request/Page`
- **Step 16**: `Go to Record/Request/Page` [draft]
- **Step 17**: `Go to Field` [draft]
- **Step 22**: `Enter Find Mode` [draft]
- **Step 41**: `Enter Preview Mode` [draft]
- **Step 55**: `Enter Browse Mode` [draft]
- **Step 74**: `Go to Related Record` [draft]
- **Step 99**: `Go to Portal Row` [draft]
- **Step 169**: `Close Popover` [draft]

### Step 4: Go to Next Field

**Status**: draft

## Description

FileMaker script step: Go to Next Field

## Mapping rules

- `name="Go to Next Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="4"` for all `Go to Next Field` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="4" name="Go to Next Field">
        </Step>

```

---

### Step 5: Go to Previous Field

**Status**: draft

## Description

FileMaker script step: Go to Previous Field

## Mapping rules

- `name="Go to Previous Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="5"` for all `Go to Previous Field` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="5" name="Go to Previous Field">
        </Step>

```

---

### Step 6: Go to Layout

**Status**: draft

## Description

element is output only if  is not "OriginalLayout."
  element is output only if  is "LayoutNameByCalc" or "LayoutNumberByCalc".
  is required in case there is more than one layout with the same name.
 element is output only if an animation value other than "None" was selected for the script step.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Go to Layout"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="6"` for all `Go to Layout` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Layout id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Layout>` element specifies the target layout.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{AnimationID}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="6" name="Go to Layout">
          <LayoutDestination value="SelectedLayout"/>
          <Layout name="LayoutName" id="1"/>
            <Calculation>
              <![CDATA[CalcString]]>
            </Calculation>
          </Layout>
  <Animation value=.../>
        </Step>
```

---

### Step 16: Go to Record/Request/Page

## Description

Navigates to a specific record, request, or page in the current found set or portal.

## Mapping rules

- `name="Go to Record/Request/Page"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="16"` for all `Go to Record/Request/Page` steps.
- The `<RowPageLocation>` child element has a `value` attribute that corresponds to the location specified:
  - `First` maps to `value="First"`.
  - `Last` maps to `value="Last"`.
  - `Next` maps to `value="Next"`.
  - `Previous` maps to `value="Previous"`.
  - When a calculation is provided (with `With dialog:`), maps to `value="ByCalculation"`.
- The `<NoInteract>` child element controls dialog display:
  - `With dialog: On` maps to `state="False"` (allows user interaction/dialog).
  - `With dialog: Off` maps to `state="True"` (suppresses dialog).
  - Defaults to `state="False"` when not specified.
- The `<Exit>` child element appears when `Exit after last:` is specified:
  - `Exit after last: On` maps to `state="True"`.
  - `Exit after last: Off` maps to `state="False"`.
  - Only present for `Next` and `Previous` when explicitly specified.
- When a calculation is provided (e.g., `$Index`), include a `<Calculation>` child element wrapped in `<![CDATA[ ... ]]>` containing the calculation expression.

## Examples

### Input (plain text)

```plaintext
Go to Record/Request/Page [ First ]
Go to Record/Request/Page [ Last ]
Go to Record/Request/Page [ Previous ; Exit after last: On ]
Go to Record/Request/Page [ Next ; Exit after last: Off ]
Go to Record/Request/Page [ With dialog: On ; $Index ]
Go to Record/Request/Page [ With dialog: Off ; $Index ]
```

### Output (XML, step-only)

```xml
<Step enable="True" id="16" name="Go to Record/Request/Page">
  <NoInteract state="False"></NoInteract>
  <RowPageLocation value="First"></RowPageLocation>
</Step>
<Step enable="True" id="16" name="Go to Record/Request/Page">
  <NoInteract state="False"></NoInteract>
  <RowPageLocation value="Last"></RowPageLocation>
</Step>
<Step enable="True" id="16" name="Go to Record/Request/Page">
  <NoInteract state="False"></NoInteract>
  <Exit state="True"></Exit>
  <RowPageLocation value="Previous"></RowPageLocation>
</Step>
<Step enable="True" id="16" name="Go to Record/Request/Page">
  <NoInteract state="False"></NoInteract>
  <Exit state="False"></Exit>
  <RowPageLocation value="Next"></RowPageLocation>
</Step>
<Step enable="True" id="16" name="Go to Record/Request/Page">
  <NoInteract state="False"></NoInteract>
  <RowPageLocation value="ByCalculation"></RowPageLocation>
  <Calculation><![CDATA[$Index]]></Calculation>
</Step>
<Step enable="True" id="16" name="Go to Record/Request/Page">
  <NoInteract state="True"></NoInteract>
  <RowPageLocation value="ByCalculation"></RowPageLocation>
  <Calculation><![CDATA[$Index]]></Calculation>
</Step>
```

---

### Step 16: Go to Record/Request/Page

**Status**: draft

## Description

and  nodes are present when

         attribute is "ByCalculation".



         element is only present when  is

        "Next" or "Previous".



         indicates whether script execution should be terminated if

        there is no next/previous record/request/page (that is, if the current

        record/request/page is the last/first one).

## Mapping rules

- `name="Go to Record/Request/Page"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="16"` for all `Go to Record/Request/Page` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="16" name="Go to Record/Request/Page">
  
          
  <NoInteract state="True"/>
  
          
  <Exit state="False"/>
  
          
  <RowPageLocation value="ByCalculation"/>
  
          
  <Calculation>
             CalcString
          </Calculation>
  
        
</Step>

```

---

### Step 17: Go to Field

**Status**: draft

## Description

FileMaker script step: Go to Field

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Go to Field"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="17"` for all `Go to Field` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="17" name="Go to Field">
  
           
  <SelectAll state="True"/>
  
           
  <Field name="FieldName" id="2" table="TableName"/>
  
           
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 22: Enter Find Mode

**Status**: draft

## Description

{See Perform Find.}

## Mapping rules

- `name="Enter Find Mode"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="22"` for all `Enter Find Mode` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See Perform Find for remaining XML.}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="22" name="Enter Find Mode">
          ...
        <Step enable="True">
```

---

### Step 41: Enter Preview Mode

**Status**: draft

## Description

FileMaker script step: Enter Preview Mode

## Mapping rules

- `name="Enter Preview Mode"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="41"` for all `Enter Preview Mode` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="41" name="Enter Preview Mode">
        </Step>

```

---

### Step 55: Enter Browse Mode

**Status**: draft

## Description

FileMaker script step: Enter Browse Mode

## Mapping rules

- `name="Enter Browse Mode"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="55"` for all `Enter Browse Mode` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="55" name="Enter Browse Mode">
        </Step>

```

---

### Step 74: Go to Related Record

**Status**: draft

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

---

### Step 99: Go to Portal Row

**Status**: draft

## Description

and  nodes are present when

           attribute is "ByCalculation".
  element is only present when  is

          "Next" or "Previous".
  indicates whether script execution should be terminated if

          there is no next/previous row in the portal (that is, if the current row is the

          last/first one in the portal).

## Mapping rules

- `name="Go to Portal Row"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="99"` for all `Go to Portal Row` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="99" name="Go to Portal Row">
  
           
  <NoInteract state="True"/>
  
           
  <SelectAll state="False"/>
  
           
  <Exit state="False"/>
  
           
  <RowPageLocation value="ByCalculation"/>
  
           
  <Calculation>
              CalcString
           </Calculation>
  
        
</Step>

```

---

### Step 169: Close Popover

**Status**: draft

## Description

FileMaker script step: Close Popover

## Mapping rules

- `name="Close Popover"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="169"` for all `Close Popover` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="169" name="Close Popover">
        </Step>

```

---

## Open Menu Item (16 steps)

- **Step 32**: `Open Help` [draft]
- **Step 38**: `Open Manage Database` [draft]
- **Step 88**: `Open Script Workspace` [draft]
- **Step 105**: `Open Preferences` [draft]
- **Step 112**: `Open Manage Value Lists` [draft]
- **Step 113**: `Open Sharing` [draft]
- **Step 114**: `Open File Options` [draft]
- **Step 118**: `<span class=` [draft]
- **Step 129**: `Open Find/Replace` [draft]
- **Step 140**: `Open Manage Data Sources` [draft]
- **Step 149**: `Open Edit Saved Finds` [draft]
- **Step 151**: `Open Manage Layouts ` [draft]
- **Step 156**: `Open Manage Containers` [draft]
- **Step 165**: `Open Manage Themes` [draft]
- **Step 172**: `Upload to FileMaker Server` [draft]
- **Step 183**: `<span class=` (vnewto16) [draft]

### Step 32: Open Help

**Status**: draft

## Description

FileMaker script step: Open Help

## Mapping rules

- `name="Open Help"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="32"` for all `Open Help` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="32" name="Open Help">
        </Step>

```

---

### Step 38: Open Manage Database

**Status**: draft

## Description

FileMaker script step: Open Manage Database

## Mapping rules

- `name="Open Manage Database"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="38"` for all `Open Manage Database` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="38" name="Open Manage Database">
        </Step>

```

---

### Step 88: Open Script Workspace

**Status**: draft

## Description

FileMaker script step: Open Script Workspace

## Mapping rules

- `name="Open Script Workspace"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="88"` for all `Open Script Workspace` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="88" name="Open Script Workspace">
        </Step>

```

---

### Step 105: Open Preferences

**Status**: draft

## Description

FileMaker script step: Open Preferences

## Mapping rules

- `name="Open Preferences"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="105"` for all `Open Preferences` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="105" name="Open Preferences">
        </Step>

```

---

### Step 112: Open Manage Value Lists

**Status**: draft

## Description

FileMaker script step: Open Manage Value Lists

## Mapping rules

- `name="Open Manage Value Lists"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="112"` for all `Open Manage Value Lists` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="112" name="Open Manage Value Lists">
        </Step>

```

---

### Step 113: Open Sharing

**Status**: draft

## Description

FileMaker script step: Open Sharing

## Mapping rules

- `name="Open Sharing"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="113"` for all `Open Sharing` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="113" name="Open Sharing">
        </Step>

```

---

### Step 114: Open File Options

**Status**: draft

## Description

FileMaker script step: Open File Options

## Mapping rules

- `name="Open File Options"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="114"` for all `Open File Options` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="114" name="Open File Options">
        </Step>

```

---

### Step 118: <span class=

**Status**: draft

## Description

FileMaker script step: <span class=

## Mapping rules

- `name="<span class="` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="118"` for all `<span class=` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="118" name="Open Hosts">
        </Step>

```

---

### Step 129: Open Find/Replace

**Status**: draft

## Description

FileMaker script step: Open Find/Replace

## Mapping rules

- `name="Open Find/Replace"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="129"` for all `Open Find/Replace` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="129" name="Open Find/Replace">
        </Step>

```

---

### Step 140: Open Manage Data Sources

**Status**: draft

## Description

FileMaker script step: Open Manage Data Sources

## Mapping rules

- `name="Open Manage Data Sources"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="140"` for all `Open Manage Data Sources` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="140" name="Open Manage Data Sources">
        </Step>

```

---

### Step 149: Open Edit Saved Finds

**Status**: draft

## Description

FileMaker script step: Open Edit Saved Finds

## Mapping rules

- `name="Open Edit Saved Finds"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="149"` for all `Open Edit Saved Finds` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="149" name="Open Edit Saved Finds">
        </Step>

```

---

### Step 151: Open Manage Layouts 

**Status**: draft

## Description

FileMaker script step: Open Manage Layouts 

## Mapping rules

- `name="Open Manage Layouts "` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="151"` for all `Open Manage Layouts ` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="151" name="Open Manage Layouts ">
        </Step>

```

---

### Step 156: Open Manage Containers

**Status**: draft

## Description

FileMaker script step: Open Manage Containers

## Mapping rules

- `name="Open Manage Containers"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="156"` for all `Open Manage Containers` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="156" name="Open Manage Containers">
        </Step>

```

---

### Step 165: Open Manage Themes

**Status**: draft

## Description

FileMaker script step: Open Manage Themes

## Mapping rules

- `name="Open Manage Themes"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="165"` for all `Open Manage Themes` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="165" name="Open Manage Themes">
        </Step>

```

---

### Step 172: Upload to FileMaker Server

**Status**: draft

## Description

FileMaker script step: Upload to FileMaker Server

## Mapping rules

- `name="Upload to FileMaker Server"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="172"` for all `Upload to FileMaker Server` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="172" name="Upload to FileMaker Server">
        </Step>

```

---

### Step 183: <span class=

**Version**: newto16

**Status**: draft

## Description

FileMaker script step: <span class=

## Mapping rules

- `name="<span class="` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="183"` for all `<span class=` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="183" name="Open My Apps">
        </Step>

```

---

## Records (16 steps)

- **Step 7**: `New Record/Request` [draft]
- **Step 8**: `Duplicate Record/Request` [draft]
- **Step 9**: `Delete Record/Request` [draft]
- **Step 10**: `Delete All Records` [draft]
- **Step 35**: `Import Records` [draft]
- **Step 36**: `Export Records` [draft]
- **Step 51**: `Revert Record/Request` [draft]
- **Step 75**: `Commit Records/Requests` [draft]
- **Step 98**: `Copy All Records/Requests` [draft]
- **Step 101**: `Copy Record/Request` [draft]
- **Step 104**: `Delete Portal Row` [draft]
- **Step 133**: `Open Record/Request` [draft]
- **Step 143**: `Save Records as Excel` [draft]
- **Step 144**: `Save Records as PDF` [draft]
- **Step 152**: `Save Records as Snapshot Link` [draft]
- **Step 182**: `Truncate Table` (vnewto15) [draft]

### Step 7: New Record/Request

**Status**: draft

## Description

FileMaker script step: New Record/Request

## Mapping rules

- `name="New Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="7"` for all `New Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="7" name="New Record/Request">
        </Step>

```

---

### Step 8: Duplicate Record/Request

**Status**: draft

## Description

FileMaker script step: Duplicate Record/Request

## Mapping rules

- `name="Duplicate Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="8"` for all `Duplicate Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="8" name="Duplicate Record/Request">
        </Step>

```

---

### Step 9: Delete Record/Request

**Status**: draft

## Description

FileMaker script step: Delete Record/Request

## Mapping rules

- `name="Delete Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="9"` for all `Delete Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="9" name="Delete Record/Request">
  
          
  <NoInteract state="True"/>
  
        
</Step>

```

---

### Step 10: Delete All Records

**Status**: draft

## Description

FileMaker script step: Delete All Records

## Mapping rules

- `name="Delete All Records"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="10"` for all `Delete All Records` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="10" name="Delete All Records">
  
          
  <NoInteract state="True"/>
  
        
</Step>

```

---

### Step 35: Import Records

**Status**: draft

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

---

### Step 36: Export Records

**Status**: draft

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

---

### Step 51: Revert Record/Request

**Status**: draft

## Description

FileMaker script step: Revert Record/Request

## Mapping rules

- `name="Revert Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="51"` for all `Revert Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="51" name="Revert Record/Request">
  
          
  <NoInteract state="True"/>
  
        
</Step>

```

---

### Step 75: Commit Records/Requests

**Status**: draft

## Description

FileMaker script step: Commit Records/Requests

## Mapping rules

- `name="Commit Records/Requests"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="75"` for all `Commit Records/Requests` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="75" name="Commit Records/Requests">
  
          
  <NoInteract state="True"/>
  
          
  <Option state="true"/>
  
        
  <ESSForceCommit state="True"/>
   
</Step>

```

---

### Step 98: Copy All Records/Requests

**Status**: draft

## Description

FileMaker script step: Copy All Records/Requests

## Mapping rules

- `name="Copy All Records/Requests"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="98"` for all `Copy All Records/Requests` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="98" name="Copy All Records/Requests">
        </Step>

```

---

### Step 101: Copy Record/Request

**Status**: draft

## Description

FileMaker script step: Copy Record/Request

## Mapping rules

- `name="Copy Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="101"` for all `Copy Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="101" name="Copy Record/Request">
        </Step>

```

---

### Step 104: Delete Portal Row

**Status**: draft

## Description

FileMaker script step: Delete Portal Row

## Mapping rules

- `name="Delete Portal Row"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="104"` for all `Delete Portal Row` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="104" name="Delete Portal Row">
  
          
  <NoInteract state="True"/>
  
        
</Step>

```

---

### Step 133: Open Record/Request

**Status**: draft

## Description

FileMaker script step: Open Record/Request

## Mapping rules

- `name="Open Record/Request"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="133"` for all `Open Record/Request` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="133" name="Open Record/Request">
        </Step>

```

---

### Step 143: Save Records as Excel

**Status**: draft

## Description

may not be generated if there is no output file specified in the script step.
 value of "XLXE" means export to "Excel workbook (.xlsx)" type.

## Mapping rules

- `name="Save Records as Excel"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="143"` for all `Save Records as Excel` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="143" name="Save Records as Excel">
  
            
  <NoInteract state="True"/>
  
            
  <Restore state="True"/>
  
            
  <AutoOpen state="True"/>
  
            
  <CreateEmail state="True"/>
  
            
  <CreateDirectories state="True"/>
  
            
  <UniversalPathList>...</UniversalPathList>
  
            
  <SaveType value="BrowsedRecords"/>
  
            
  <UseFieldNames state="True"/>
  
            
  <WorkSheet>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </WorkSheet>
  
            
  <Title>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </Title>
  
            
  <Subject>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </Subject>
  
            
  <Author>
    
                
    <Calculation>
                CalcString
                </Calculation>
    
            
  </Author>
  
        
</Step>

```

---

### Step 144: Save Records as PDF

**Status**: draft

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

---

### Step 152: Save Records as Snapshot Link

**Status**: draft

## Description

FileMaker script step: Save Records as Snapshot Link

## Mapping rules

- `name="Save Records as Snapshot Link"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="152"` for all `Save Records as Snapshot Link` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{PathList}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="152" name="Save Records as Snapshot Link">
  
             
  <CreateEmail state="True"/>
  
             
  <CreateDirectories state="True"/>
  
             
  <UniversalPathList>...</UniversalPathList>
  
             
  <SaveType value="BrowsedRecords"/>
  
         
</Step>

```

---

### Step 182: Truncate Table

**Version**: newto15

**Status**: draft

## Description

If  is not "", the ID and name reflect the specified table.

## Mapping rules

- `name="Truncate Table"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="182"` for all `Truncate Table` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="182" name="Truncate Table">
  
           
  <NoInteract state="False"/>
  
           
  <BaseTable id="-1" name="&lt;Current Table&gt;"/>
  
        
</Step>

```

---

## Sort/Find/Print (2 steps)

- **Step 42**: `Print Setup` [draft]
- **Step 43**: `Print` [draft]

### Step 42: Print Setup

**Status**: draft

## Description

FileMaker script step: Print Setup

## Mapping rules

- `name="Print Setup"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="42"` for all `Print Setup` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Flattened Windows/Mac specific
        settings}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="42" name="Print Setup">
          <NoInteract state="False"/>
          <Restore state="true">
              <![CDATA[...]]>
          </Format>
        </Step>
```

---

### Step 43: Print

**Status**: draft

## Description

FileMaker script step: Print

## Mapping rules

- `name="Print"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="43"` for all `Print` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{Flattened Windows/Mac specific
        settings}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="43" name="Print">
          <NoInteract state="True"/>
          <Restore state="true">
              <![CDATA[...]]>
        </Step>
```

---

## Spelling (7 steps)

- **Step 18**: `Check Selection` [draft]
- **Step 19**: `Check Record` [draft]
- **Step 20**: `Check Found Set` [draft]
- **Step 106**: `Correct Word` [draft]
- **Step 107**: `Spelling Options` [draft]
- **Step 108**: `Select Dictionaries` [draft]
- **Step 109**: `Edit User Dictionary` [draft]

### Step 18: Check Selection

**Status**: draft

## Description

FileMaker script step: Check Selection

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Check Selection"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="18"` for all `Check Selection` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Field id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Field>` element specifies the target field.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="18" name="Check Selection">
  
          
  <SelectAll state="True"/>
  
          
  <Field name="f2" id="2" table="test"/>
  
          
  <Repetition>
    
             
    <Calculation>
               &quot;Value&quot;
             </Calculation>
    
           
  </Repetition>
  
        
</Step>

```

---

### Step 19: Check Record

**Status**: draft

## Description

FileMaker script step: Check Record

## Mapping rules

- `name="Check Record"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="19"` for all `Check Record` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="19" name="Check Record">
        </Step>

```

---

### Step 20: Check Found Set

**Status**: draft

## Description

FileMaker script step: Check Found Set

## Mapping rules

- `name="Check Found Set"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="20"` for all `Check Found Set` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="20" name="Check Found Set">
        </Step>

```

---

### Step 106: Correct Word

**Status**: draft

## Description

FileMaker script step: Correct Word

## Mapping rules

- `name="Correct Word"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="106"` for all `Correct Word` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="106" name="Correct Word">
        </Step>

```

---

### Step 107: Spelling Options

**Status**: draft

## Description

FileMaker script step: Spelling Options

## Mapping rules

- `name="Spelling Options"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="107"` for all `Spelling Options` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="107" name="Spelling Options">
        </Step>

```

---

### Step 108: Select Dictionaries

**Status**: draft

## Description

FileMaker script step: Select Dictionaries

## Mapping rules

- `name="Select Dictionaries"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="108"` for all `Select Dictionaries` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="108" name="Select Dictionaries">
        </Step>

```

---

### Step 109: Edit User Dictionary

**Status**: draft

## Description

FileMaker script step: Edit User Dictionary

## Mapping rules

- `name="Edit User Dictionary"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="109"` for all `Edit User Dictionary` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="109" name="Edit User Dictionary">
        </Step>

```

---

## Windows (16 steps)

- **Step 29**: `Show/Hide Toolbars` [draft]
- **Step 30**: `View As` [draft]
- **Step 31**: `Adjust Window` [draft]
- **Step 79**: `Freeze Window` [draft]
- **Step 80**: `Refresh Window` [draft]
- **Step 81**: `Scroll Window` [draft]
- **Step 92**: `Show/Hide Text Ruler` [draft]
- **Step 97**: `Set Zoom Level` [draft]
- **Step 119**: `Move/Resize Window` [draft]
- **Step 120**: `Arrange All Windows` [draft]
- **Step 121**: `Close Window` [draft]
- **Step 122**: `New Window` [draft]
- **Step 123**: `Select Window` [draft]
- **Step 124**: `Set Window Title` [draft]
- **Step 166**: `Show/Hide Menubar` [draft]
- **Step 174**: `Enable Touch Keyboard` [draft]

### Step 29: Show/Hide Toolbars

**Status**: draft

## Description

FileMaker script step: Show/Hide Toolbars

## Mapping rules

- `name="Show/Hide Toolbars"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="29"` for all `Show/Hide Toolbars` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="29" name="Show/Hide Toolbars">
  
          
  <Lock state="True"/>
  
          
  <ShowHide value="Hide"/>
  
        
</Step>

```

---

### Step 30: View As

**Status**: draft

## Description

FileMaker script step: View As

## Mapping rules

- `name="View As"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="30"` for all `View As` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="30" name="View As">
  
           
  <View value="Form"/>
  
        
</Step>

```

---

### Step 31: Adjust Window

**Status**: draft

## Description

FileMaker script step: Adjust Window

## Mapping rules

- `name="Adjust Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="31"` for all `Adjust Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="31" name="Adjust Window">
  
          
  <WindowState value="Maximize"/>
  
        
</Step>

```

---

### Step 79: Freeze Window

**Status**: draft

## Description

FileMaker script step: Freeze Window

## Mapping rules

- `name="Freeze Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="79"` for all `Freeze Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="79" name="Freeze Window">
        </Step>

```

---

### Step 80: Refresh Window

**Status**: draft

## Description

corresponds to the "flush cached join results" option.
 corresponds to the "flush cached SQL data" option.

## Mapping rules

- `name="Refresh Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="80"` for all `Refresh Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="80" name="Refresh Window">
  
          
  <Option state="True"/>
  
          
  <FlushSQLData state="True"/>
  
        
</Step>

```

---

### Step 81: Scroll Window

**Status**: draft

## Description

FileMaker script step: Scroll Window

## Mapping rules

- `name="Scroll Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="81"` for all `Scroll Window` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="81" name="Scroll Window">
  
          
  <ScrollOperation value="Home"/>
  
        
</Step>

```

---

### Step 92: Show/Hide Text Ruler

**Status**: draft

## Description

FileMaker script step: Show/Hide Text Ruler

## Mapping rules

- `name="Show/Hide Text Ruler"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="92"` for all `Show/Hide Text Ruler` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="92" name="Show/Hide Text Ruler">
  
          
  <ShowHide value="Hide"/>
  
        
</Step>

```

---

### Step 97: Set Zoom Level

**Status**: draft

## Description

FileMaker script step: Set Zoom Level

## Mapping rules

- `name="Set Zoom Level"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="97"` for all `Set Zoom Level` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="97" name="Set Zoom Level">
  
          
  <Lock state="True"/>
  
          
  <Zoom value="75"/>
  
        
</Step>

```

---

### Step 119: Move/Resize Window

**Status**: draft

## Description

{See New Window.}

## Mapping rules

- `name="Move/Resize Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="119"` for all `Move/Resize Window` steps.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{See New Window for remaining XML}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="119" name="Move/Resize Window">
  
          
  <Window value="Current"/>
  
          ...
        
</Step>

```

---

### Step 120: Arrange All Windows

**Status**: draft

## Description

FileMaker script step: Arrange All Windows

## Mapping rules

- `name="Arrange All Windows"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="120"` for all `Arrange All Windows` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="120" name="Arrange All Windows">
  
          
  <WindowArrangement value="TileHorizontally"/>
  
        
</Step>

```

---

### Step 121: Close Window

**Status**: draft

## Description

is present when  is "ByName".

## Mapping rules

- `name="Close Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="121"` for all `Close Window` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="121" name="Close Window">
  
          
  <Window value="ByName"/>
  
          
  <Name>
    
            
    <Calculation>
              &quot;Customer Name&quot;
            </Calculation>
    
          
  </Name>
  
        
</Step>

```

---

### Step 122: New Window

**Status**: draft

## Description

element is output only
          if  is not "OriginalLayout."
  element is output only if  is "LayoutNameByCalc" or "LayoutNumberByCalc."
  is required in case there is more than one layout with the same name.

**Note**: This step may reference database-specific IDs (layout, table, field, etc.).
See `meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="New Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="122"` for all `New Window` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.
- **Do not** include a `Layout id="…"` attribute; see `meta/layout-and-object-ids.md`.
- `<Layout>` element specifies the target layout.
- **Conditional elements**: Some elements may only appear under certain conditions:
  - `{value}` - appears conditionally

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="122" name="New Window">
  
          
  <Name>
    
            
    <Calculation>
              &quot;WindowName&quot;
            </Calculation>
    
          
  </Name>
  
          
  <Height>
    
            
    <Calculation>
              200
            </Calculation>
    
          
  </Height>
  
          
  <Width>
    
            
    <Calculation>
              400
            </Calculation>
    
          
  </Width>
  
          
  <DistanceFromTop>
    
            
    <Calculation>
              100
            </Calculation>
    
          
  </DistanceFromTop>
  
          
  <DistanceFromLeft>
    
            
    <Calculation>
              125
            </Calculation>
    
          
  </DistanceFromLeft>
  
   
  <NewWndStyles Style="Dialog" Close="Yes" Minimize="No" Maximize="Yes" Resize="Yes" MenuBar="Yes" DimParentWindow="No" Styles="..."/>
  
  
  <LayoutDestination value="SelectedLayout"/>
  
            
  <Layout name="LayoutName" id="1"/>
  
        
</Step>

```

---

### Step 123: Select Window

**Status**: draft

## Description

is present when  is "ByName".

## Mapping rules

- `name="Select Window"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="123"` for all `Select Window` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="123" name="Select Window">
  
          
  <Window value="ByName"/>
  
          
  <Name>
    
            
    <Calculation>
              &quot;Customer Name&quot;
            </Calculation>
    
          
  </Name>
  
        
</Step>

```

---

### Step 124: Set Window Title

**Status**: draft

## Description

is present when  is "ByName".

## Mapping rules

- `name="Set Window Title"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="124"` for all `Set Window Title` steps.
- `<Calculation>` contains the calculation expression, wrapped in `<![CDATA[ ... ]]>`.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="124" name="Set Window Title">
  
          
  <Window value="ByName"/>
  
          
  <Name>
    
            
    <Calculation>
              &quot;Customer Name&quot;
            </Calculation>
    
          
  </Name>
  
          
  <NewName>
    
            
    <Calculation>
              &quot;New Title&quot;
            </Calculation>
    
          
  </NewName>
  
        
</Step>

```

---

### Step 166: Show/Hide Menubar

**Status**: draft

## Description

FileMaker script step: Show/Hide Menubar

## Mapping rules

- `name="Show/Hide Menubar"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="166"` for all `Show/Hide Menubar` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="166" name="Show/Hide Menubar">
  
          
  <Lock state="True"/>
  
          
  <ShowHide value="Toggle"/>
  
        
</Step>

```

---

### Step 174: Enable Touch Keyboard

**Status**: draft

## Description

FileMaker script step: Enable Touch Keyboard

## Mapping rules

- `name="Enable Touch Keyboard"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="174"` for all `Enable Touch Keyboard` steps.

## Examples

### Output (XML, step-only)

```xml
<Step enable="True" id="174" name="Enable Touch Keyboard">
  
            
  <ShowHide value="Hide"/>
  
        
</Step>

```

---

# FileMaker Functions

The following functions are commonly used in FileMaker calculations.
Functions appear inside `<![CDATA[ ... ]]>` blocks in XML and are preserved exactly as written.

## Get

**Signature**: `Get ( state )`

**Status**: draft

## Description

Returns information about the current FileMaker environment, window, script, or record state, depending on the `state` parameter.

In this project, `Get ( ... )` values are always used **inside calculations** that end up inside `<![CDATA[ ... ]]>` in XML. The XML mapping never changes based on the specific `Get` state; only the calculation text does.

## Arguments

- **state**: A keyword indicating which value to retrieve, such as:
  - `LayoutName`
  - `ScriptParameter`
  - `WindowMode`
  - `WindowLeft`
  - `WindowTop`
  - `RecordNumber`
  - `FoundCount`
  - `ScriptResult`

## Return value

- A value whose type depends on `state` (for example, text for `LayoutName`, number for `WindowMode`, etc.).

## Usage notes

- In calculations, `Get` is usually nested inside other functions (for example `GetValue ( Get ( ScriptParameter ) ; 1 )`) or used in boolean expressions (for example `Get ( WindowMode ) = 1`).
- For txt2xml purposes, **do not rewrite or normalize** the `Get` expression; copy it verbatim into `<![CDATA[ ... ]]>`.

## Examples

### Example: store current layout name

```plaintext
Set Variable [ $previousLayout ; Value: Get (LayoutName) ]
```

XML calculation:

```xml
<Calculation><![CDATA[Get (LayoutName)]]></Calculation>
```

### Example: window mode check

```plaintext
If [ Get ( WindowMode ) = 1 ]
```

XML calculation:

```xml
<Calculation><![CDATA[Get ( WindowMode ) = 1]]></Calculation>
```

---

## GetValue

**Signature**: `GetValue ( text ; number )`

**Status**: draft

## Description

Returns the value from a return-delimited list at the specified line number.

Commonly used with `Get ( ScriptParameter )` to pull one parameter out of a multi-line script parameter.

## Arguments

- **text**: A return-delimited list of values.
- **number**: 1-based index of the value to return.

## Return value

- The text value at the specified line; empty if the index is out of range.

## Usage notes

- For txt2xml, `GetValue` is always part of a calculation copied verbatim into `<![CDATA[ ... ]]>`.
- Do not reorder arguments or add extra whitespace beyond what appears in the source.

## Examples

### Example: first parameter from script parameter

```plaintext
Set Variable [ $input ; Value: GetValue ( Get ( ScriptParameter ) ; 1 ) ]
```

XML calculation:

```xml
<Calculation><![CDATA[GetValue ( Get ( ScriptParameter ) ; 1 )]]></Calculation>
```

---

## IsEmpty

**Signature**: `IsEmpty ( fieldOrExpression )`

**Status**: draft

## Description

Returns true if the specified field or expression is empty; otherwise false.

Commonly used in `If` conditions to drive error handling or control flow.

## Arguments

- **fieldOrExpression**: A field reference or calculation expression whose emptiness should be tested.

## Return value

- Boolean (true/false), represented in FileMaker as 1 (true) or 0 (false) in numeric contexts.

## Usage notes

- Often combined with the logical `not` operator, for example `not IsEmpty ( $missingEmail )`.
- For txt2xml, the entire `IsEmpty` expression (including any surrounding `not`) is preserved exactly inside `<![CDATA[ ... ]]>`.

## Examples

### Example: check if a variable is empty

```plaintext
If [ IsEmpty ( $committeeMemberId ) ]
```

XML calculation:

```xml
<Calculation><![CDATA[IsEmpty ( $committeeMemberId )]]></Calculation>
```

### Example: fire error if a variable is not empty

```plaintext
If [ not IsEmpty ( $missingEmail ) ]
```

XML calculation:

```xml
<Calculation><![CDATA[not IsEmpty ( $missingEmail )]]></Calculation>
```

---

## JSONGetElement

**Signature**: `JSONGetElement ( json ; keyOrPath )`

**Status**: draft

## Description

Extracts a value from a JSON object or array at the specified key or path.

## Arguments

- **json**: A JSON string.
- **keyOrPath**: A key or path expression indicating which element to retrieve (for example `"layout"` or `"members[0].id"`).

## Return value

- The value located at the given key/path, as text/JSON depending on context, or an empty string if not found.

## Usage notes

- Often used to unpack JSON stored in variables (for example `$input`).
- For txt2xml, the entire function call is preserved exactly inside `<![CDATA[ ... ]]>`.

## Examples

### Example: extract `"layout"` from JSON input

```plaintext
Set Variable [ $layout ; Value: JSONGetElement ( $input ; "layout" ) ]
```

XML calculation:

```xml
<Calculation><![CDATA[JSONGetElement ( $input ; "layout" )]]></Calculation>
```

---

## JSONSetElement

**Signature**: `JSONSetElement ( json ; [ keyOrPath ; value ; type ] { ; ... } )`

**Status**: draft

## Description

Sets one or more elements in a JSON object or array and returns the updated JSON string.

## Arguments

- **json**: A JSON string to modify (often `"{}"` for a new object).
- **[ keyOrPath ; value ; type ]**: One or more triplets specifying:
  - **keyOrPath**: Key or path where the value should be stored (for example `"error"` or `"members[0].id"`).
  - **value**: The value to assign.
  - **type**: A JSON type keyword such as `JSONString`, `JSONNumber`, `JSONArray`, etc.

## Return value

- A JSON string with all specified elements set/updated.

## Usage notes

- Commonly used to build structured JSON results for script outputs.
- txt2xml should **not** try to interpret the JSON semantics; it only needs to preserve the function call exactly inside `<![CDATA[ ... ]]>`.

## Examples

### Example: simple error JSON

```plaintext
Set Variable [ $ResultMessage ; Value: JSONSetElement ( "{}" ; "error" ; $error_message ; JSONString ) ]
```

XML calculation:

```xml
<Calculation><![CDATA[JSONSetElement ( "{}" ; "error" ; $error_message ; JSONString )]]></Calculation>
```

### Example: success result with `ok` and `members`

```plaintext
Set Variable [ $ResultMessages ; Value:   JSONSetElement ( "{}" ;
    [ "ok" ; 1 ; JSONNumber ] ;
    [ "members" ; $members ; JSONArray ]
  ) ]
```

XML calculation:

```xml
<Calculation><![CDATA[  JSONSetElement ( "{}" ;
    [ "ok" ; 1 ; JSONNumber ] ;
    [ "members" ; $members ; JSONArray ]
  )]]></Calculation>
```

---

# Important Policies

## Database-Specific IDs

Some XML attributes (like `Layout id`, `Table id`, `Field id`) are database-specific and cannot be inferred from plain text.

**Critical rules**:

- **Never guess or fabricate** these IDs
- **Omit the `id` attribute** and use only `name` (or calculation)
- **Add a helper comment step** before steps that reference named objects, containing the original plain text

See the individual step documentation above for specific guidance.

## Calculation Preservation

All calculations are preserved **exactly as written** inside `<![CDATA[ ... ]]>` blocks.
The converter does not:

- Rewrite or normalize function calls
- Change whitespace
- Reorder parameters
- Interpret function semantics
