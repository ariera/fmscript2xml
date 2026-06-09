---
id: 210
name: "Perform Script on Server with Callback"
category: Control
status: draft
input_patterns:
  - "Perform Script on Server with Callback [ ... ]"
fm_name: "Perform Script on Server with Callback"
xml:
  step_name: "Perform Script on Server with Callback"
  enable_default: True
  wrapper: step-only
---

## Description

Runs a server-side script and registers a client-side callback script that is
invoked when the server script completes. Both the server script and the
callback script can be specified either from list (a named reference requiring
database-specific IDs) or by name (a calculated reference).

**Note**: This step may reference database-specific IDs (script IDs). See
`meta/layout-and-object-ids.md` for the policy on handling these IDs.

## Mapping rules

- `name="Perform Script on Server with Callback"` in the `<Step>` element.
- `enable="True"` unless the step is explicitly disabled in the text.
- `id="210"` for all `Perform Script on Server with Callback` steps.
- `<CallbackScriptState value="..."/>` reflects the `State` parameter
  (`Continue`, `Halt`, `Exit`, `Resume`, `Pause`).
- `<Calculation>` holds the server script parameter, wrapped in `<![CDATA[ ... ]]>`.
- The server script reference is `<Script name="..."/>` when specified from list,
  or `<Calculated><Calculation>...</Calculation></Calculated>` when specified by name.
  A calculated server script reference appears before `<CallbackScriptState>`.
- `<CallbackScript>` wraps the callback script reference
  (`<ScriptName name="..."/>` from list, or `<Calculated>` by name) and its
  `<ScriptParameter><Calculation>...</Calculation></ScriptParameter>`.
- A helper comment preserving the original text is emitted when a script is
  specified from list, since the named references require manual ID resolution.

## Examples

### Output (XML, step-only)
