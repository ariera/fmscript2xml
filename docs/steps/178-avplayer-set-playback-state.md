---
id: 178
name: "AVPlayer Set Playback State"
category: Miscellaneous
status: draft
input_patterns:
  - "AVPlayer Set Playback State [ ... ]"
fm_name: "AVPlayer Set Playback State"
xml:
  step_name: "AVPlayer Set Playback State"
  enable_default: True
  wrapper: step-only
---

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
