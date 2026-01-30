## Layout and object IDs in generated XML

Some FileMaker XML attributes (for example layout `id`, table `id`, field `id`) are **database-specific**. Their numeric values depend on the structure of a particular FileMaker file and **cannot be inferred** from the plain text script steps alone.

Because of this, when generating XML from plain text, the converter must:

- **Never guess or fabricate** any `id` attribute for:
  - `<Layout id="…">`
  - `<Table id="…">`
  - `<Field id="…">`
  - Or any other element where the id is not derivable from the user’s input and requires knowledge of the specific FileMaker file.
- Instead, **omit the `id` attribute entirely** and rely on the `name` (or calculation) so the XML is still valid and safely editable by a developer.

### Helper comment for developer intervention

When a script step depends on a database-specific id that cannot be resolved (for example `Go to Layout` targeting a specific layout), the converter should:

1. **Insert a comment step immediately before the affected step**, containing the original plain-text script step.
2. Generate the actual step **without** the unresolved `id` attribute, but with the correct `name` and other attributes.

This makes the XML:

- Safe and valid.
- Easier for a FileMaker developer to review and manually add the correct `id` values later, using the preceding comment as a reference.

### Example: `Go to Layout`

Plain text:

```plaintext
Go to Layout [ “Developer” (SYS__System) ; Animation: None ]
```

Actual XML in one specific database (note the layout id is database-specific and not portable):

```xml
<fmxmlsnippet type="FMObjectList">
  <Step enable="True" id="6" name="Go to Layout">
    <LayoutDestination value="SelectedLayout"></LayoutDestination>
    <Layout id="435" name="Developer"></Layout>
  </Step>
</fmxmlsnippet>
```

Generated XML that the converter should produce (no `id` on `<Layout>`, plus a helper comment step):

```xml
<fmxmlsnippet type="FMObjectList">
  <Step enable="True" id="89" name="# (comment)">
    <Text>Go to Layout [ “Developer” (SYS__System) ; Animation: None ]</Text>
  </Step>
  <Step enable="True" id="6" name="Go to Layout">
    <LayoutDestination value="SelectedLayout"></LayoutDestination>
    <Layout name="Developer"></Layout>
  </Step>
</fmxmlsnippet>
```

Other steps that require database-specific ids (for example ones that reference specific layouts, tables, or fields) must follow the **same pattern**:

- Do not emit an `id` attribute you cannot know.
- Optionally precede the step with a comment containing the original plain-text step so a developer can complete the id manually.


