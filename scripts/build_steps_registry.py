#!/usr/bin/env python3
"""
Build step registry JSON from markdown files.

This script extracts minimal step metadata from docs/steps/*.md files
and creates a compact JSON file for runtime use.

Usage:
    python scripts/build_steps_registry.py
"""

import json
import re
import sys
import yaml
from pathlib import Path


def extract_step_data(md_file: Path) -> dict:
    """
    Extract minimal step data from markdown file.

    Only extracts the 4 fields needed at runtime:
    - id: Step ID number
    - name: Step name for matching
    - xml_step_name: Name to use in XML <Step> element
    - enable_default: Default enable state
    """
    try:
        content = md_file.read_text(encoding='utf-8')

        # Extract YAML frontmatter
        yaml_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not yaml_match:
            print(f"Warning: No YAML frontmatter found in {md_file.name}", file=sys.stderr)
            return None

        yaml_content = yaml_match.group(1)
        metadata = yaml.safe_load(yaml_content)

        if not metadata:
            print(f"Warning: Empty YAML metadata in {md_file.name}", file=sys.stderr)
            return None

        # Extract required fields
        step_id = metadata.get('id')
        name = metadata.get('name')

        if step_id is None or not name:
            print(f"Warning: Missing id or name in {md_file.name}", file=sys.stderr)
            return None

        # Extract XML info
        xml_info = metadata.get('xml', {})
        xml_step_name = xml_info.get('step_name', name)
        enable_default = xml_info.get('enable_default', True)

        return {
            'id': step_id,
            'name': name,
            'xml_step_name': xml_step_name,
            'enable_default': enable_default
        }

    except Exception as e:
        print(f"Error processing {md_file.name}: {e}", file=sys.stderr)
        return None


def main():
    """Build step registry JSON from markdown files."""
    # Determine paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    docs_steps_dir = project_root / 'docs' / 'steps'
    output_dir = project_root / 'src' / 'fmscript2xml' / 'data'
    output_file = output_dir / 'steps.json'

    # Check source directory exists
    if not docs_steps_dir.exists():
        print(f"Error: Source directory not found: {docs_steps_dir}", file=sys.stderr)
        return 1

    # Create output directory if needed
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process all markdown files
    steps = {}
    skipped = []

    for md_file in sorted(docs_steps_dir.glob('*.md')):
        # Skip index file
        if md_file.name == '_index.md':
            continue

        step_data = extract_step_data(md_file)
        if step_data:
            steps[step_data['name']] = step_data
        else:
            skipped.append(md_file.name)

    # Write JSON file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(steps, f, indent=2, sort_keys=True)

        print(f"✓ Successfully built step registry")
        print(f"  Source: {docs_steps_dir}")
        print(f"  Output: {output_file}")
        print(f"  Steps: {len(steps)}")

        if skipped:
            print(f"  Skipped: {len(skipped)} files")
            for name in skipped:
                print(f"    - {name}")

        return 0

    except Exception as e:
        print(f"Error writing output file: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
