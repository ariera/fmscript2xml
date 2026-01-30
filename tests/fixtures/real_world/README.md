## Real-World Script Fixtures

This directory holds real-world FileMaker script fixtures for integration tests.

Each fixture folder should contain:

- `input.txt`: plain text script
- `expected.xml`: XML exported from FileMaker (clipboard fmxmlsnippet)
- `metadata.json` (optional): known differences or notes

### Adding a Fixture

1. Create a directory under `tests/fixtures/real_world/` with a clear name.
2. Save the plain text script as `input.txt`.
3. Export the script steps from FileMaker to XML and save as `expected.xml`.
4. (Optional) Add `metadata.json` for notes.

### Notes

- The tests use semantic comparison, so expected XML can include IDs that will be ignored.
- Helper comments inserted by the converter (e.g., `Original:`) are ignored.
