"""
Loader for step definitions from markdown files.

Parses YAML frontmatter and extracts step metadata from docs/steps/.
"""

import re
import yaml
from pathlib import Path
from typing import Dict, List, Optional
from .step_def import StepDefinition, MappingRule, ConditionalElement, XMLTemplate


class StepRegistry:
    """Registry of FileMaker script step definitions."""

    def __init__(self, steps_dir: Optional[Path] = None):
        """
        Initialize registry.

        Args:
            steps_dir: Path to docs/steps directory.
                      If None, uses relative path from this file.
        """
        if steps_dir is None:
            # Default: docs/steps (from project root)
            base_dir = Path(__file__).parent.parent.parent.parent
            steps_dir = base_dir / "docs" / "steps"

        self.steps_dir = Path(steps_dir)
        self._definitions: Dict[str, StepDefinition] = {}
        self._definitions_by_id: Dict[int, StepDefinition] = {}
        self._loaded = False

    def load_all(self) -> None:
        """Load all step definitions from markdown files."""
        if self._loaded:
            return

        if not self.steps_dir.exists():
            raise FileNotFoundError(
                f"Steps directory not found: {self.steps_dir}. "
                "Please ensure docs/steps exists."
            )

        # Load all .md files
        for md_file in self.steps_dir.glob("*.md"):
            if md_file.name == "_index.md":
                continue

            try:
                step_def = self._load_step_definition(md_file)
                if step_def:
                    self._definitions[step_def.name] = step_def
                    self._definitions_by_id[step_def.id] = step_def
            except Exception as e:
                # Log error but continue loading other steps
                print(f"Warning: Failed to load {md_file.name}: {e}")

        self._loaded = True

    def _load_step_definition(self, md_file: Path) -> Optional[StepDefinition]:
        """Load a single step definition from markdown file."""
        content = md_file.read_text(encoding='utf-8')

        # Extract YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not yaml_match:
            return None

        yaml_content = yaml_match.group(1)
        metadata = yaml.safe_load(yaml_content)

        if not metadata:
            return None

        # Extract basic info
        step_id = metadata.get('id', 0)
        name = metadata.get('name', '')
        category = metadata.get('category', '')
        status = metadata.get('status', 'draft')
        input_patterns = metadata.get('input_patterns', [])
        fm_name = metadata.get('fm_name', name)

        xml_info = metadata.get('xml', {})
        xml_step_name = xml_info.get('step_name', name)
        enable_default = xml_info.get('enable_default', True)
        wrapper = xml_info.get('wrapper', 'step-only')

        # Extract description and examples from markdown
        markdown_body = content[yaml_match.end():]
        description = self._extract_description(markdown_body)
        examples = self._extract_examples(markdown_body)

        # Check if step requires database IDs
        requires_db_ids = 'database-specific IDs' in markdown_body or \
                         'layout-and-object-ids.md' in markdown_body

        # Extract mapping rules
        mapping_rules = self._extract_mapping_rules(markdown_body, requires_db_ids)

        # Extract conditional elements
        conditional_elements = self._extract_conditional_elements(markdown_body)

        return StepDefinition(
            id=step_id,
            name=name,
            category=category,
            status=status,
            input_patterns=input_patterns,
            fm_name=fm_name,
            enable_default=enable_default,
            wrapper=wrapper,
            xml_step_name=xml_step_name,
            mapping_rules=mapping_rules,
            conditional_elements=conditional_elements,
            requires_db_ids=requires_db_ids,
            description=description,
            examples=examples
        )

    def _extract_description(self, markdown: str) -> str:
        """Extract description from markdown."""
        # Look for ## Description section
        desc_match = re.search(r'## Description\n\n(.*?)(?=\n##|\Z)', markdown, re.DOTALL)
        if desc_match:
            return desc_match.group(1).strip()
        return ""

    def _extract_examples(self, markdown: str) -> List[Dict[str, str]]:
        """Extract examples from markdown."""
        examples = []

        # Look for example blocks
        example_pattern = r'### (?:Example \d+|Input.*?)\n\n```(?:plaintext|text)\n(.*?)```\n\n(?:### Output.*?\n\n)?```xml\n(.*?)```'
        matches = re.finditer(example_pattern, markdown, re.DOTALL)

        for match in matches:
            input_text = match.group(1).strip()
            output_xml = match.group(2).strip()
            examples.append({
                'input': input_text,
                'output': output_xml
            })

        return examples

    def _extract_mapping_rules(self, markdown: str, requires_db_ids: bool) -> List[MappingRule]:
        """Extract mapping rules from markdown."""
        rules = []

        # Look for mapping rules section
        rules_match = re.search(r'## Mapping rules\n\n(.*?)(?=\n##|\Z)', markdown, re.DOTALL)
        if not rules_match:
            return rules

        rules_text = rules_match.group(1)

        # Parse bullet points
        for line in rules_text.split('\n'):
            line = line.strip()
            if not line.startswith('-'):
                continue

            # Check for calculation
            if '<Calculation>' in line:
                rules.append(MappingRule(
                    rule_type='calculation',
                    requires_cdata=True
                ))

            # Check for field references
            if '<Field' in line:
                rules.append(MappingRule(
                    rule_type='field',
                    target_element='Field',
                    omit_id=requires_db_ids
                ))

            # Check for layout references
            if '<Layout' in line:
                rules.append(MappingRule(
                    rule_type='layout',
                    target_element='Layout',
                    omit_id=requires_db_ids
                ))

            # Check for table references
            if '<Table' in line:
                rules.append(MappingRule(
                    rule_type='table',
                    target_element='Table',
                    omit_id=requires_db_ids
                ))

        return rules

    def _extract_conditional_elements(self, markdown: str) -> List[ConditionalElement]:
        """Extract conditional elements from markdown."""
        elements = []

        # Look for conditional elements section
        cond_match = re.search(
            r'- \*\*Conditional elements\*\*:.*?\n((?:  - .*\n?)+)',
            markdown,
            re.DOTALL
        )
        if not cond_match:
            return elements

        cond_text = cond_match.group(1)
        for line in cond_text.split('\n'):
            line = line.strip()
            if line.startswith('- `'):
                # Extract element name and description
                match = re.match(r'- `([^`]+)` - (.+)', line)
                if match:
                    element_name = match.group(1)
                    description = match.group(2)
                    elements.append(ConditionalElement(
                        element_name=element_name,
                        condition="",  # Would need more parsing to extract condition
                        description=description
                    ))

        return elements

    def get(self, step_name: str) -> Optional[StepDefinition]:
        """Get step definition by name."""
        if not self._loaded:
            self.load_all()

        # Try exact match first
        step_def = self._definitions.get(step_name)
        if step_def:
            return step_def

        # Try with trailing space (parser strips trailing spaces, but registry might have them)
        if not step_name.endswith(' '):
            step_def = self._definitions.get(step_name + ' ')
            if step_def:
                return step_def

        # Try without trailing space (registry has space, but parser strips it)
        step_name_stripped = step_name.rstrip()
        if step_name_stripped != step_name:
            step_def = self._definitions.get(step_name_stripped)
            if step_def:
                return step_def

        return None

    def get_by_id(self, step_id: int) -> Optional[StepDefinition]:
        """Get step definition by ID."""
        if not self._loaded:
            self.load_all()
        return self._definitions_by_id.get(step_id)

    def all_steps(self) -> List[StepDefinition]:
        """Get all step definitions."""
        if not self._loaded:
            self.load_all()
        return list(self._definitions.values())

    def step_names(self) -> List[str]:
        """Get all step names."""
        if not self._loaded:
            self.load_all()
        return list(self._definitions.keys())

