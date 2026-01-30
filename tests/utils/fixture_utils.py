"""Fixture utilities for real-world script tests."""

from __future__ import annotations

from pathlib import Path
from typing import List, Optional

from .ddr_ir_loader import load_ddr_ir, get_step_reference_xml


def create_fixture(script_name: str, input_text: str, expected_xml: str) -> Path:
    """Create a fixture folder with input.txt and expected.xml."""
    base_dir = Path(__file__).resolve().parents[1] / "fixtures" / "real_world"
    fixture_dir = base_dir / script_name
    fixture_dir.mkdir(parents=True, exist_ok=True)

    (fixture_dir / "input.txt").write_text(input_text, encoding="utf-8")
    (fixture_dir / "expected.xml").write_text(expected_xml, encoding="utf-8")

    return fixture_dir


def validate_fixture(fixture_path: Path) -> bool:
    """Validate that a fixture has required files."""
    fixture_path = Path(fixture_path)
    return (fixture_path / "input.txt").exists() and (fixture_path / "expected.xml").exists()


def list_fixtures() -> List[Path]:
    """List all fixture directories under tests/fixtures/real_world."""
    base_dir = Path(__file__).resolve().parents[1] / "fixtures" / "real_world"
    if not base_dir.exists():
        return []
    return [p for p in base_dir.iterdir() if p.is_dir() and not p.name.startswith('.')]


def generate_reference_from_ddr_ir(step_id: int) -> Optional[str]:
    """Generate fmxmlsnippet XML from DDR IR reference for a step."""
    steps_dir = Path(__file__).resolve().parents[3] / "docs" / "DRR XML Grammar" / "ddr-ir" / "steps"
    load_ddr_ir(steps_dir)
    step_xml = get_step_reference_xml(step_id)
    if not step_xml:
        return None

    # Replace placeholders with minimal valid values so XML can be parsed
    step_xml = _replace_placeholders(step_xml)

    return _wrap_in_fmxmlsnippet(step_xml)


def _replace_placeholders(xml: str) -> str:
    """Replace DDR IR placeholders with minimal valid values for XML parsing."""
    import re

    # Common placeholders and their minimal replacements
    replacements = {
        '{name}': 'test',
        '{PathList}': '',
        '{OLE data}': '',
        '{Object Type}': 'File',
        '{AnimationID}': '0',
        '{Animation}': 'None',
        '{Script step text}': '',
        '{Table}': 'Table1',
        '{FieldName}': 'Field1',
        '{CalcString}': '"Calculation"',
        '{TextString}': '"Text"',
        '{TargetName}': 'Target',
        '{TargetType}': 'Type',
        '{class}': 'class1',
        '{id}': '1',
        '{QueryText}': 'Query',
        '{http}': 'http://example.com',
        '{CatalogName}': 'Catalog',
        '{compiled apple script data}': '',
    }

    result = xml

    # Remove comment-like placeholders (not real placeholders, just notes)
    # These should be removed entirely - they describe conditional XML blocks
    # These placeholders can contain XML and span multiple lines

    # First, remove simple comment placeholders
    result = re.sub(r'\{See Perform Find for remaining XML\.\}', '', result)
    result = re.sub(r'\{Flattened[^}]*\}', '', result, flags=re.DOTALL)

    # Remove complex multi-line conditional blocks like {for ... data source : ... }
    # These can contain XML tags, so we need to match braces carefully
    # Pattern: {for ... : ... } - match from {for to matching }
    def remove_conditional_block(match):
        # This is called for each {for ... } block
        return ''

    # Match {for ... : ... } and {For ... : ... } blocks (can span multiple lines and contain XML)
    # We'll match from {for/{For to the closing } that's at the same brace level
    # This is tricky because the content can have XML tags with attributes
    # We need to count braces to find the matching }
    def remove_conditional_blocks(text, pattern):
        """Remove conditional blocks matching pattern (e.g., '{for' or '{For')."""
        pos = 0
        while pos < len(text):
            # Find next match
            match_pos = text.find(pattern, pos)
            if match_pos == -1:
                break

            # Find the matching closing brace
            brace_count = 0
            close_pos = match_pos
            while close_pos < len(text):
                if text[close_pos] == '{':
                    brace_count += 1
                elif text[close_pos] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        # Found matching brace
                        text = text[:match_pos] + text[close_pos+1:]
                        pos = match_pos  # Check from same position again
                        break
                close_pos += 1
            else:
                # No matching brace found, skip this one
                pos = match_pos + 1
        return text

    # Remove both {for and {For patterns
    result = remove_conditional_blocks(result, '{for')
    result = remove_conditional_blocks(result, '{For')

    # Remove any remaining very long placeholders (likely conditional blocks we missed)
    result = re.sub(r'\{[^}]{200,}\}', '', result, flags=re.DOTALL)

    # Remove comment-like placeholders first (not real placeholders, just notes)
    # These should be removed entirely before other processing
    comment_placeholders = [
        r'\{See Perform Find for remaining XML\.\}',
        r'\{for [^}]+\}',
    ]
    for pattern in comment_placeholders:
        result = re.sub(pattern, '', result)

    # FIRST: Fix attribute placeholders - they need to be quoted
    # Pattern: attribute_name={placeholder} -> attribute_name="replacement"
    # This must happen BEFORE simple text replacement
    # Use a more general pattern that matches any attribute with {placeholder}
    for placeholder, replacement in replacements.items():
        # Extract the placeholder content (without the braces)
        placeholder_content = placeholder.strip('{}')
        # Match: word + = + { + placeholder_content + }
        # Replace with: word + = + " + replacement + "
        # We need to escape the braces in the pattern
        pattern = rf'(\w+)=\{{{re.escape(placeholder_content)}\}}'
        result = re.sub(pattern, rf'\1="{replacement}"', result)

    # SECOND: Do simple text replacements for content (not attributes)
    for placeholder, replacement in replacements.items():
        result = result.replace(placeholder, replacement)

    # Remove attributes with remaining placeholder values that we couldn't replace
    # Match: whitespace + word + = + { + anything + }
    result = re.sub(r'\s+\w+=\{[^}]+\}', '', result)

    # Fix malformed XML - remove duplicate closing tags
    result = re.sub(r'</StepText>\s*</StepText>', '</StepText>', result)

    # Remove orphaned closing tags (closing tag without opening tag)
    result = re.sub(r'\s*</StepText>\s*', '', result)

    # Remove empty StepText elements
    result = re.sub(r'<StepText>\s*</StepText>', '', result)

    # Fix incomplete CDATA sections (malformed in DDR IR)
    # Pattern: <![CDATA[ ... </Calculation> where CDATA is not properly closed
    # Some DDR IR has incomplete CDATA like <![CDATA[<Step ...> without closing ]]>
    def fix_incomplete_cdata(text):
        # Find CDATA sections that don't end with ]]>
        # Pattern: <![CDATA[ ... </Tag> where ... doesn't contain ]]>
        pattern = r'<!\[CDATA\[([^\]]*?)(</[^>]+>)'
        def fix_match(m):
            content = m.group(1)
            closing_tag = m.group(2)
            # If content doesn't end with ]]>, fix it
            if ']]>' not in content:
                # Remove any incomplete XML tags from content
                content = re.sub(r'<[^>]*$', '', content)  # Remove incomplete tag at end
                content = re.sub(r'<Step[^>]*>', '', content)  # Remove incomplete Step tags
                return f'<![CDATA[{content}]]>{closing_tag}'
            return m.group(0)
        return re.sub(pattern, fix_match, text, flags=re.DOTALL)

    result = fix_incomplete_cdata(result)

    # Fix unclosed tags - find opening tags without closing tags and close them
    # This handles malformed DDR IR XML like unclosed <DisplayCalculation>, <SMTPEncryptionType>, etc.
    # Common tags that might be unclosed in DDR IR
    unclosed_tags = ['DisplayCalculation', 'Calculated', 'StepText', 'Query', 'RequestRow',
                     'SMTPEncryptionType', 'SMTPAuthenticationType', 'Layout', 'Field', 'Script',
                     'ChgPwdOnNextLogin', 'AccountName', 'ContentType', 'UniversalPathList',
                     'TargetName', 'TargetType', 'TextString', 'CalcString', 'InputFields',
                     'Document', 'DisplayCalculation', 'InputField', 'With', 'Author', 'KeyWords',
                     'AllPages', 'InsertFrom', 'ScanFrom', 'BarCodes', 'Calculation', 'Repetition']

    # Close unclosed tags - close each tag before the next opening tag of the same type or before parent/Step
    def close_unclosed_tags_smart(text):
        # For each tag in unclosed_tags list, find unclosed instances and close them
        for tag in unclosed_tags:
            # Find all opening tags of this type
            tag_opens = list(re.finditer(rf'<{re.escape(tag)}([^>]*?)>', text))
            if not tag_opens:
                continue

            # Find all closing tags of this type
            tag_closes = list(re.finditer(rf'</{re.escape(tag)}>', text))

            # Process from the end to avoid position shifts
            for tag_match in reversed(tag_opens):
                attrs = tag_match.group(1)
                # Skip if self-closing
                if attrs.strip().endswith('/'):
                    continue

                open_end = tag_match.end()
                after_open = text[open_end:]

                # Check if this tag is closed
                next_close = re.search(rf'</{re.escape(tag)}>', after_open)

                # Check for next opening tag of same type (for nested structures like InputField)
                next_open = re.search(rf'<{re.escape(tag)}([^>]*?)(?<!/)>', after_open)

                # Check for parent closing (e.g., </InputFields> for <InputField>)
                parent_close = None
                if tag == 'InputField':
                    parent_close = re.search(r'</InputFields>', after_open)

                # Check for Step closing
                step_close = re.search(r'(</Step>|</ScriptStep>)', after_open)

                # Determine where to close
                close_pos = None
                if next_open and (not next_close or next_open.start() < next_close.start()):
                    # Close before next opening tag of same type
                    close_pos = open_end + next_open.start()
                elif next_close:
                    # Already has closing tag, skip
                    continue
                elif parent_close:
                    # Close before parent
                    close_pos = open_end + parent_close.start()
                elif step_close:
                    # Close before Step
                    close_pos = open_end + step_close.start()

                if close_pos:
                    text = text[:close_pos] + f'\n          </{tag}>' + text[close_pos:]

        return text

    result = close_unclosed_tags_smart(result)

    # Fix step 144: Remove orphaned closing tags for Author and KeyWords immediately after close_unclosed_tags_smart
    # This needs to happen early to prevent issues later
    author_opens = len(re.findall(r'<Author[^>]*>', result))
    author_closes = len(re.findall(r'</Author>', result))
    if author_closes > author_opens:
        extra = author_closes - author_opens
        author_close_matches = list(re.finditer(r'</Author>', result))
        for m in reversed(author_close_matches[-extra:]):
            result = result[:m.start()] + result[m.end():]

    keywords_opens = len(re.findall(r'<KeyWords[^>]*>', result))
    keywords_closes = len(re.findall(r'</KeyWords>', result))
    if keywords_closes > keywords_opens:
        extra = keywords_closes - keywords_opens
        keywords_close_matches = list(re.finditer(r'</KeyWords>', result))
        for m in reversed(keywords_close_matches[-extra:]):
            result = result[:m.start()] + result[m.end():]

    # Fix step 164: DisplayCalculation should close right after Calculation, not after all other elements
    # The structure is malformed: <DisplayCalculation><Calculation>...</DisplayCalculation>...</Calculation>
    # Should be: <DisplayCalculation><Calculation>...</Calculation></DisplayCalculation>
    def fix_displaycalculation_structure(text):
        # Find </DisplayCalculation> that appears before a </Calculation>
        display_close_match = re.search(r'</DisplayCalculation>', text)
        if display_close_match:
            after_display_close = text[display_close_match.end():]
            calc_close_match = re.search(r'</Calculation>', after_display_close)
            if calc_close_match:
                # DisplayCalculation closes before Calculation - this is wrong
                # Check if there's a Calculation before DisplayCalculation
                before_display = text[:display_close_match.start()]
                calc_before = re.search(r'<Calculation[^>]*>', before_display)
                if calc_before:
                    # Find the </Calculation> that should close the Calculation opened before DisplayCalculation
                    after_calc_open = before_display[calc_before.end():]
                    calc_close_before = re.search(r'</Calculation>', after_calc_open)
                    if calc_close_before:
                        # Move </DisplayCalculation> to right after </Calculation>
                        calc_close_pos = calc_before.end() + calc_close_before.start() + len('</Calculation>')
                        # Remove </DisplayCalculation> from current position
                        text = text[:display_close_match.start()] + text[display_close_match.end():]
                        # Add it after </Calculation>
                        text = text[:calc_close_pos] + '\n          </DisplayCalculation>' + text[calc_close_pos:]

        return text

    result = fix_displaycalculation_structure(result)

    # Fix step 87: Empty InputField tags - if InputField has no content, it should be self-closing or removed
    def fix_empty_inputfields(text):
        # Find <InputFields>...</InputFields> blocks
        inputfields_pattern = r'<InputFields>.*?</InputFields>'
        def fix_inputfields_block(match):
            block = match.group(0)
            # Find empty InputField tags: <InputField...></InputField> with nothing or just whitespace between
            # Pattern: <InputField[^>]*>\s*</InputField>
            empty_pattern = r'<InputField([^>]*)>\s*</InputField>'
            # Replace with self-closing
            fixed = re.sub(empty_pattern, r'<InputField\1/>', block)
            return fixed

        return re.sub(inputfields_pattern, fix_inputfields_block, text, flags=re.DOTALL)

    result = fix_empty_inputfields(result)

    # Fix step 161: Unclosed InsertFrom tag
    def fix_unclosed_insertfrom(text):
        insertfrom_opens = len(re.findall(r'<InsertFrom[^>]*>', text))
        insertfrom_closes = len(re.findall(r'</InsertFrom>', text))
        if insertfrom_opens > insertfrom_closes:
            # Find the last InsertFrom opening tag and add closing tag before </Step>
            last_insertfrom = list(re.finditer(r'<InsertFrom[^>]*>', text))
            if last_insertfrom:
                last_match = last_insertfrom[-1]
                after_insertfrom = text[last_match.end():]
                # Find </Step> and insert </InsertFrom> before it
                step_close = re.search(r'</Step>', after_insertfrom)
                if step_close:
                    insert_pos = last_match.end() + step_close.start()
                    text = text[:insert_pos] + '\n           </InsertFrom>' + text[insert_pos:]
        return text

    result = fix_unclosed_insertfrom(result)

    # Fix step 144: Orphaned closing tags and unclosed Document tag
    def fix_step_144_structure(text):
        # Remove orphaned closing tags for Author and KeyWords
        # Simple approach: count opens and closes, remove extra closes from the end
        author_opens = len(re.findall(r'<Author[^>]*>', text))
        author_closes = len(re.findall(r'</Author>', text))
        if author_closes > author_opens:
            # Remove the last (author_closes - author_opens) closing tags
            extra = author_closes - author_opens
            author_close_matches = list(re.finditer(r'</Author>', text))
            # Remove from the end
            for m in reversed(author_close_matches[-extra:]):
                text = text[:m.start()] + text[m.end():]

        keywords_opens = len(re.findall(r'<KeyWords[^>]*>', text))
        keywords_closes = len(re.findall(r'</KeyWords>', text))
        if keywords_closes > keywords_opens:
            # Remove the last (keywords_closes - keywords_opens) closing tags
            extra = keywords_closes - keywords_opens
            keywords_close_matches = list(re.finditer(r'</KeyWords>', text))
            # Remove from the end
            for m in reversed(keywords_close_matches[-extra:]):
                text = text[:m.start()] + text[m.end():]

        # Also remove orphaned closing tags after </Step>
        step_close_match = re.search(r'</Step>', text)
        if step_close_match:
            after_step = text[step_close_match.end():]
            # Remove any closing tags after </Step> (except </fmxmlsnippet>)
            after_step_cleaned = re.sub(r'</(?!fmxmlsnippet)\w+>', '', after_step)
            text = text[:step_close_match.end()] + after_step_cleaned

        # Fix Document tag structure - Document should close after AllPages, not before
        # Find </Document> that appears before </AllPages>
        document_close_match = re.search(r'</Document>', text)
        if document_close_match:
            after_document_close = text[document_close_match.end():]
            allpages_close_match = re.search(r'</AllPages>', after_document_close)
            if allpages_close_match:
                # Document closes before AllPages - this is wrong
                # Move </Document> to after </AllPages>
                allpages_close_pos = document_close_match.end() + allpages_close_match.end()
                # Remove </Document> from current position
                text = text[:document_close_match.start()] + text[document_close_match.end():]
                # Add it after </AllPages>
                text = text[:allpages_close_pos - len('</Document>')] + '\n            </Document>' + text[allpages_close_pos - len('</Document>'):]

        # If Document still doesn't close, add it after Security
        document_opens = len(re.findall(r'<Document[^>]*>', text))
        document_closes = len(re.findall(r'</Document>', text))
        if document_opens > document_closes:
            # Find </Security> and add </Document> after it
            security_close_match = re.search(r'</Security>', text)
            if security_close_match:
                insert_pos = security_close_match.end()
                text = text[:insert_pos] + '\n            </Document>' + text[insert_pos:]

        return text

    result = fix_step_144_structure(result)

    # Fix step 164: DisplayCalculation structure - it should close right after Calculation
    def fix_step_164_displaycalculation(text):
        # Pattern: <DisplayCalculation><Calculation>...other elements...</Calculation></Step>
        # The issue is that other elements like <WaitForCompletion> are inside <Calculation>, which is wrong
        # But we can't fix the structure - we just need to close DisplayCalculation after Calculation closes
        displaycalc_match = re.search(r'<DisplayCalculation[^>]*>', text)
        if displaycalc_match:
            after_displaycalc = text[displaycalc_match.end():]
            # Find the Calculation inside DisplayCalculation
            calc_match = re.search(r'<Calculation[^>]*>', after_displaycalc)
            if calc_match:
                after_calc_open = after_displaycalc[calc_match.end():]
                # Find the </Calculation> that closes this Calculation
                calc_close_match = re.search(r'</Calculation>', after_calc_open)
                if calc_close_match:
                    # Always close DisplayCalculation right after Calculation closes
                    calc_close_pos = displaycalc_match.end() + calc_match.end() + calc_close_match.end()
                    # Remove any existing </DisplayCalculation> (but keep track of where it was)
                    existing_displaycalc_close = re.search(r'</DisplayCalculation>', text)
                    if existing_displaycalc_close:
                        text = text[:existing_displaycalc_close.start()] + text[existing_displaycalc_close.end():]
                        # Adjust calc_close_pos if the removed tag was before it
                        if existing_displaycalc_close.start() < calc_close_pos:
                            calc_close_pos -= len('</DisplayCalculation>')
                    # Insert </DisplayCalculation> right after </Calculation> (before </Step> if it's there)
                    # Check if </Step> immediately follows </Calculation>
                    after_calc_close_text = text[calc_close_pos:]
                    step_close_immediately = re.match(r'\s*</Step>', after_calc_close_text)
                    if step_close_immediately:
                        # Insert before </Step>
                        text = text[:calc_close_pos] + '\n          </DisplayCalculation>' + text[calc_close_pos:]
                    else:
                        # Insert right after </Calculation>
                        text = text[:calc_close_pos] + '\n          </DisplayCalculation>' + text[calc_close_pos:]

        return text

    result = fix_step_164_displaycalculation(result)

    # Fix step 161: Multiple Step blocks and malformed attributes
    # The DDR IR contains multiple examples - we should only keep the first complete one
    def fix_step_161_multiple_steps(text):
        # Find the first complete <Step>...</Step> block
        first_step_match = re.search(r'<Step[^>]*>', text)
        if first_step_match:
            after_first_step = text[first_step_match.end():]
            # Find the first </Step> that closes this Step
            first_step_close = re.search(r'</Step>', after_first_step)
            if first_step_close:
                # Keep only up to the first complete Step block
                first_complete_end = first_step_match.end() + first_step_close.end()
                # Check if there are more Step blocks
                remaining = text[first_complete_end:]
                if '<Step' in remaining:
                    # Remove all subsequent Step blocks
                    # Find the position before </fmxmlsnippet>
                    fmxmlsnippet_close = re.search(r'</fmxmlsnippet>', remaining)
                    if fmxmlsnippet_close:
                        # Keep only the first Step and close properly
                        text = text[:first_complete_end] + '\n</fmxmlsnippet>'

        # Fix malformed attributes like Choice="front"|"Back" or Choice="full"|"medium"|"large"
        # Remove all parts after the first quoted value by removing everything from |" to the closing quote
        # Pattern: Choice="value1"|"value2"|"value3" -> Choice="value1"
        text = re.sub(r'(\|"[^"]*")+', '', text)  # Remove all |"value" sequences

        # Fix unquoted attribute values like Types=<barcode_bitmask32>
        # Remove these attributes entirely as they're invalid
        text = re.sub(r'\s+\w+=<[^>]+>', '', text)

        # Fix malformed tags like <InsertFrom value="Video Camera"/StepText>
        text = re.sub(r'<InsertFrom([^>]*)/StepText>', r'<InsertFrom\1>', text)
        text = re.sub(r'<InsertFrom([^>]*)/>', r'<InsertFrom\1></InsertFrom>', text)

        # Fix unclosed InsertFrom tags
        insertfrom_opens = len(re.findall(r'<InsertFrom[^>]*>', text))
        insertfrom_closes = len(re.findall(r'</InsertFrom>', text))
        if insertfrom_opens > insertfrom_closes:
            # Find the last InsertFrom and close it before </Step>
            last_insertfrom = list(re.finditer(r'<InsertFrom[^>]*>', text))
            if last_insertfrom:
                last_match = last_insertfrom[-1]
                after_insertfrom = text[last_match.end():]
                step_close = re.search(r'</Step>', after_insertfrom)
                if step_close:
                    insert_pos = last_match.end() + step_close.start()
                    text = text[:insert_pos] + '\n           </InsertFrom>' + text[insert_pos:]

        return text

    result = fix_step_161_multiple_steps(result)

    # Fix self-closing tags that have children (malformed XML in DDR IR)
    # Pattern: <TagName .../> ... </TagName>
    # Convert to: <TagName ...> ... </TagName>
    # This is a common issue in DDR IR where tags are self-closing but have children
    def fix_self_closing_with_children(text):
        # Find all closing tags and check if there's a matching self-closing tag before them
        # Process in reverse to handle nested cases correctly
        closing_tag_pattern = r'</(\w+)>'
        closing_tags = list(re.finditer(closing_tag_pattern, text))

        # Process from right to left
        for closing_match in reversed(closing_tags):
            tag_name = closing_match.group(1)
            close_pos = closing_match.start()

            # Look backwards for matching self-closing tag
            # Pattern: <tag_name .../> before this closing tag
            before_close = text[:close_pos]
            # Find the last occurrence of <tag_name .../>
            self_closing_pattern = rf'<{re.escape(tag_name)}([^>]*)/>'
            self_closing_matches = list(re.finditer(self_closing_pattern, before_close))

            if self_closing_matches:
                # Get the last (closest) match
                self_closing_match = self_closing_matches[-1]
                open_pos = self_closing_match.start()
                attrs = self_closing_match.group(1)

                # Check if there's content between them (not just whitespace)
                content = text[self_closing_match.end():close_pos].strip()
                # Only convert if there's actual XML content (tags), not just whitespace or self-closing tags
                if content and content.startswith('<'):
                    # Make sure the content is not just self-closing tags
                    # If content is only self-closing tags, don't convert
                    non_self_closing = re.search(r'<[^/!?][^>]*>', content)  # Opening tag (not self-closing)
                    if non_self_closing:
                        # Convert self-closing to opening tag
                        text = (text[:self_closing_match.start()] +
                               f'<{tag_name}{attrs}>' +
                               text[self_closing_match.end():])

        return text

    result = fix_self_closing_with_children(result)

    # Remove closing tags for self-closing elements
    # If we have <Tag .../> followed by </Tag>, remove the closing tag
    # This handles cases where DDR IR has both self-closing and closing tag
    def remove_duplicate_closing_tags(text):
        # Find self-closing tags and remove any following closing tag of the same name
        # Pattern: <TagName .../> ... </TagName>
        self_closing_pattern = r'<(\w+)([^>]*)/>'
        for match in list(re.finditer(self_closing_pattern, text)):
            tag_name = match.group(1)
            # Look for closing tag after this self-closing tag
            after_pos = match.end()
            closing_pattern = rf'</{re.escape(tag_name)}>'
            closing_match = re.search(closing_pattern, text[after_pos:])
            if closing_match:
                # Remove the closing tag
                close_start = after_pos + closing_match.start()
                close_end = after_pos + closing_match.end()
                text = text[:close_start] + text[close_end:]
        return text

    result = remove_duplicate_closing_tags(result)

    # Remove empty elements that might have been created
    result = re.sub(r'<(\w+)\s*/>\s*', '', result)

    # Remove malformed nested Step tags (some DDR IR has <Step> inside <Step>)
    # First, handle missing </Step> - add it if needed, then remove inner Steps
    def fix_step_structure(text):
        # Check if we have <Step> but no </Step>
        has_step_open = '<Step' in text and '</Step>' not in text
        if has_step_open:
            # Add closing tag first
            text = text.rstrip() + '\n        </Step>'

        # Now handle multiple Step blocks - keep only the first complete one
        all_opens = list(re.finditer(r'<Step[^>]*>', text))
        all_closes = list(re.finditer(r'</Step>', text))

        if not all_opens or not all_closes:
            return text

        if len(all_opens) > 1 and len(all_closes) > 1:
            # Multiple Step blocks - keep only the first complete one
            first_close = all_closes[0]
            text = text[:first_close.end()]
        elif len(all_opens) == 1 and len(all_closes) > 1:
            # One opening but multiple closes - remove extra closes, keep only the last
            last_close = all_closes[-1]
            # Remove all closes except the last one
            for close_match in reversed(all_closes[:-1]):
                text = text[:close_match.start()] + text[close_match.end():]
        elif len(all_opens) > 1 and len(all_closes) == 1:
            # Multiple openings but one close - remove extra openings
            first_open = all_opens[0]
            last_close = all_closes[0]
            content_after_first = text[first_open.end():last_close.start()]
            # Remove all <Step> tags in the content
            content_after_first = re.sub(r'<Step[^>]*>', '', content_after_first)
            text = text[:first_open.end()] + content_after_first + text[last_close.start():]

        return text

    result = fix_step_structure(result)

    # Remove orphaned closing tags (closing tags without opening tags)
    # Pattern: </TagName> where there's no matching <TagName> before it
    def remove_orphaned_closing_tags(text):
        # Find all closing tags
        closing_tags = list(re.finditer(r'</(\w+)>', text))
        for closing_match in reversed(closing_tags):
            tag_name = closing_match.group(1)
            close_pos = closing_match.start()

            # Look backwards for matching opening tag
            before_close = text[:close_pos]
            # Check if there's an opening tag (not self-closing, not comment/processing instruction)
            opening_pattern = rf'<{re.escape(tag_name)}([^>]*?)(?<!/)>'
            opening_match = re.search(opening_pattern, before_close)
            if not opening_match:
                # Also check if it's a self-closing tag - if so, the closing tag is orphaned
                self_closing_pattern = rf'<{re.escape(tag_name)}[^>]*/>'
                self_closing_match = re.search(self_closing_pattern, before_close)
                if self_closing_match:
                    # There's a self-closing tag, so this closing tag is orphaned
                    text = text[:close_pos] + text[closing_match.end():]
                elif tag_name not in ['Step']:  # Don't remove </Step> as it might be needed
                    # No opening tag found at all, this is orphaned - remove it
                    text = text[:close_pos] + text[closing_match.end():]

        return text

    result = remove_orphaned_closing_tags(result)

    # Fix specific malformed structures
    # Step 42, 43: <Restore ...>...CDATA...</Format> should be <Restore ...>...CDATA...</Restore>
    result = re.sub(r'(<Restore[^>]*>.*?<!\[CDATA\[.*?\]\]>)\s*</Format>', r'\1</Restore>', result, flags=re.DOTALL)

    # Fix unclosed Sort tags (step 39: last Sort is missing closing tag)
    # If we have <SortList> with multiple <Sort> tags, ensure they're all closed
    def fix_unclosed_sort_tags(text):
        # Find <SortList> sections
        sortlist_pattern = r'(<SortList>.*?</SortList>)'
        def fix_sortlist(match):
            sortlist_content = match.group(1)
            # Count Sort opens and closes
            sort_opens = len(re.findall(r'<Sort[^>]*>', sortlist_content))
            sort_closes = len(re.findall(r'</Sort>', sortlist_content))
            sort_self = len(re.findall(r'<Sort[^>]*/>', sortlist_content))

            # If we have more opens than closes+self, add missing closes
            if sort_opens > sort_closes + sort_self:
                # Find the last <Sort> that's not self-closing and doesn't have a closing tag
                sort_matches = list(re.finditer(r'<Sort([^>]*?)(?<!/)>', sortlist_content))
                for sort_match in reversed(sort_matches):
                    after_sort = sortlist_content[sort_match.end():]
                    # Check if this Sort has a closing tag
                    if '</Sort>' not in after_sort[:after_sort.find('</SortList>')]:
                        # This Sort is not closed, close it before </SortList>
                        close_pos = sortlist_content.find('</SortList>')
                        sortlist_content = (sortlist_content[:close_pos] +
                                          '\n            </Sort>' +
                                          sortlist_content[close_pos:])
                        break
            return sortlist_content
        return re.sub(sortlist_pattern, fix_sortlist, text, flags=re.DOTALL)

    result = fix_unclosed_sort_tags(result)

    # Fix unclosed Restore tags (steps 42, 43)
    # If we have <Restore ...> (opening tag, not self-closing) but no </Restore>, add it before </Step>
    def fix_unclosed_restore(text):
        # Check if we have <Restore> (opening tag, not self-closing) without </Restore>
        restore_opens = re.findall(r'<Restore[^>]*>', text)
        restore_self_closing = re.findall(r'<Restore[^>]*/>', text)
        has_opening = any(not tag.endswith('/>') for tag in restore_opens)

        if has_opening and '</Restore>' not in text:
            # We have an opening Restore tag but no closing tag
            text = re.sub(r'(</Step>)', r'          </Restore>\n        \1', text, count=1)
        return text

    result = fix_unclosed_restore(result)

    # Fix mismatched opening/closing tags
    # Some DDR IR has <ScriptStep> but closes with </Step>
    # Change </Step> to </ScriptStep> if opening tag is <ScriptStep>
    if '<ScriptStep' in result and '</ScriptStep>' not in result:
        # Find the last </Step> and replace it with </ScriptStep>
        # This should be the closing tag for ScriptStep
        last_step_close = list(re.finditer(r'</Step>', result))
        if last_step_close:
            # Replace the last one
            last_match = last_step_close[-1]
            result = result[:last_match.start()] + '</ScriptStep>' + result[last_match.end():]

    # Remove orphaned </Script> tags (they might be added incorrectly)
    # If we have </Script> but no opening <Script> (not ScriptStep), remove it
    if '</Script>' in result and '<Script' not in result.replace('<ScriptStep', ''):
        result = re.sub(r'</Script>', '', result)

    # Fix step 39: last Sort tag is missing closing tag
    # The original has 3 Sort tags but only 2 closing tags (the last one is missing)
    # Find the last <Sort> that doesn't have a closing tag and add it before </SortList>
    def fix_missing_sort_close(text):
        # Count only <Sort> tags (not <SortList>)
        sort_opens = len(re.findall(r'<Sort\s+', text))  # <Sort followed by space (not SortList)
        sort_closes = len(re.findall(r'</Sort>', text))
        sort_self = len(re.findall(r'<Sort[^>]*/>', text))

        # If we have more opens than closes+self, add missing closes
        if sort_opens > sort_closes + sort_self:
            # Find </SortList> and add missing </Sort> before it
            sortlist_close = re.search(r'</SortList>', text)
            if sortlist_close:
                # Check if there's already a </Sort> right before </SortList>
                before_sortlist = text[:sortlist_close.start()].rstrip()
                if not before_sortlist.endswith('</Sort>'):
                    missing_count = sort_opens - sort_closes - sort_self
                    # Add missing </Sort> tags before </SortList>
                    for _ in range(missing_count):
                        text = text[:sortlist_close.start()] + '\n            </Sort>' + text[sortlist_close.start():]
                        # Update the position for next insertion
                        sortlist_close = re.search(r'</SortList>', text)
        return text

    result = fix_missing_sort_close(result)

    # Remove duplicate </Sort> tags right before </SortList>
    # Pattern: </Sort> (whitespace) </Sort> before </SortList> - keep only one
    result = re.sub(r'(</Sort>\s*){2,}(?=\s*</SortList>)', '</Sort>', result)

    # Fix malformed CDATA with spaces: <! [CDATA[ should be <![CDATA[
    result = re.sub(r'<!\s*\[CDATA\[', '<![CDATA[', result)
    # Also fix ] ]> to ]]>
    result = re.sub(r'\]\s*\]\s*>', ']]>', result)

    # Fix closing tags with spaces: </Tag > should be </Tag>
    result = re.sub(r'</(\w+)\s+>', r'</\1>', result)

    # Final cleanup: ensure all opening tags have closing tags before </Step>
    # This is a best-effort fix for malformed DDR IR XML
    return result


def _wrap_in_fmxmlsnippet(step_xml: str) -> str:
    return f'<?xml version="1.0" ?>\n<fmxmlsnippet type="FMObjectList">\n  {step_xml}\n</fmxmlsnippet>\n'
