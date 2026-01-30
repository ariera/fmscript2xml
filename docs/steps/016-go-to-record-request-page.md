---
id: 16
name: "Go to Record/Request/Page"
category: "Navigation"
status: "stable"
input_patterns:
  - "Go to Record/Request/Page [ First ]"
  - "Go to Record/Request/Page [ Last ]"
  - "Go to Record/Request/Page [ Next ]"
  - "Go to Record/Request/Page [ Previous ]"
  - "Go to Record/Request/Page [ Next ; Exit after last: On ]"
  - "Go to Record/Request/Page [ Next ; Exit after last: Off ]"
  - "Go to Record/Request/Page [ Previous ; Exit after last: On ]"
  - "Go to Record/Request/Page [ Previous ; Exit after last: Off ]"
  - "Go to Record/Request/Page [ With dialog: On ; ${calculation} ]"
  - "Go to Record/Request/Page [ With dialog: Off ; ${calculation} ]"
fm_name: "Go to Record/Request/Page"
xml:
  step_name: "Go to Record/Request/Page"
  enable_default: true
  wrapper: "step-only"
---

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

