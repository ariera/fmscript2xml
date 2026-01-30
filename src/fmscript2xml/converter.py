"""
Main converter class for FileMaker script to XML conversion.

Orchestrates the parser → registry → generator pipeline.
"""

from typing import List, Optional
from xml.etree import ElementTree as ET

from .parser.parser import Parser, ParsedStep
from .registry.loader import StepRegistry
from .registry.step_def import StepDefinition
from .generator.step_handlers import generate_xml
from .generator.xml_builder import create_fmxmlsnippet, to_xml_string


class UnknownStepError(Exception):
    """Raised when an unknown script step is encountered."""

    def __init__(self, step_name: str, line_number: int = 0):
        self.step_name = step_name
        self.line_number = line_number
        super().__init__(
            f"Unknown script step: {step_name}"
            + (f" (line {line_number})" if line_number else "")
        )


class Converter:
    """
    Main converter for FileMaker script to XML.

    Usage:
        converter = Converter()
        xml = converter.convert("Set Variable [ $var ; Value: 1 ]")
    """

    def __init__(self, steps_dir: Optional[str] = None):
        """
        Initialize converter.

        Args:
            steps_dir: Path to docs/steps directory.
                      If None, uses default relative path.
        """
        self.parser = Parser()
        self.registry = StepRegistry(steps_dir)
        self.registry.load_all()

    def convert(self, text: str, stop_on_error: bool = True) -> str:
        """
        Convert plain text FileMaker script to XML.

        Args:
            text: Plain text script
            stop_on_error: If True, raise exception on unknown step.
                          If False, skip unknown steps and continue.

        Returns:
            XML string wrapped in fmxmlsnippet

        Raises:
            UnknownStepError: If unknown step encountered and stop_on_error=True
        """
        # Parse text into steps
        parsed_steps = self.parser.parse(text)

        # Convert each step to XML
        xml_steps: List[ET.Element] = []
        errors: List[str] = []

        for parsed_step in parsed_steps:
            try:
                step_elements = self._convert_step(parsed_step, stop_on_error)
                xml_steps.extend(step_elements)
            except UnknownStepError as e:
                if stop_on_error:
                    raise
                errors.append(str(e))
            except Exception as e:
                if stop_on_error:
                    raise
                errors.append(f"Error converting step '{parsed_step.name}': {e}")

        # Create fmxmlsnippet wrapper
        root = create_fmxmlsnippet(xml_steps)

        # Convert to string
        xml_string = to_xml_string(root, pretty=True)

        # Add error comments if any
        if errors:
            # Prepend error comments
            error_comments = '\n'.join(
                f'  <!-- ERROR: {error} -->' for error in errors
            )
            xml_string = xml_string.replace(
                '<fmxmlsnippet type="FMObjectList">',
                f'<fmxmlsnippet type="FMObjectList">\n{error_comments}'
            )

        return xml_string

    def _convert_step(
        self,
        parsed_step: ParsedStep,
        stop_on_error: bool
    ) -> List[ET.Element]:
        """
        Convert a single parsed step to XML elements.

        Args:
            parsed_step: Parsed step
            stop_on_error: Whether to raise on unknown step

        Returns:
            List of XML elements (may include helper comments)

        Raises:
            UnknownStepError: If step is unknown and stop_on_error=True
        """
        # Look up step definition
        step_def = self.registry.get(parsed_step.name)

        if not step_def:
            if stop_on_error:
                raise UnknownStepError(parsed_step.name, parsed_step.line_number)
            # Return empty list to skip
            return []

        # Generate XML using handler
        return generate_xml(parsed_step, step_def)

    def validate(self, text: str) -> tuple:
        """
        Validate script text without converting.

        Args:
            text: Plain text script

        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        parsed_steps = self.parser.parse(text)
        errors = []

        for step in parsed_steps:
            if step.is_comment:
                continue

            step_def = self.registry.get(step.name)
            if not step_def:
                errors.append(
                    f"Unknown step '{step.name}' at line {step.line_number}"
                )

        return len(errors) == 0, errors


def main():
    """Command-line entry point."""
    import sys
    import argparse
    from pathlib import Path
    from . import __version__

    parser = argparse.ArgumentParser(
        description=f'Convert FileMaker script to XML (version {__version__})',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  %(prog)s script.txt              # Creates script.txt.xml
  %(prog)s script.txt -o output.xml # Creates output.xml
  %(prog)s script.txt --validate    # Only validates, no output
  %(prog)s script.txt --clipboard   # Converts and copies to clipboard (macOS only)
        """
    )
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    parser.add_argument('input', help='Input file (plain text)')
    parser.add_argument(
        '-o', '--output',
        help='Output file (XML). If not specified, creates input.xml next to input file.'
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help='Only validate, do not convert'
    )
    parser.add_argument(
        '--continue-on-error',
        action='store_true',
        help='Continue processing on errors'
    )
    parser.add_argument(
        '-c', '--clipboard',
        action='store_true',
        help='Copy result to clipboard as FileMaker objects (macOS only). '
             'Can be pasted directly into FileMaker Pro.'
    )
    parser.add_argument(
        '--no-file',
        action='store_true',
        help='Do not write output file (use with --clipboard)'
    )

    args = parser.parse_args()

    # Resolve input path
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        return 1

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        # Create output file next to input with .xml extension
        output_path = input_path.with_suffix(input_path.suffix + '.xml')

    # Read input
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        return 1

    # Convert
    converter = Converter()

    if args.validate:
        is_valid, errors = converter.validate(text)
        if is_valid:
            print("Script is valid.")
            return 0
        else:
            print("Script has errors:")
            for error in errors:
                print(f"  - {error}")
            return 1

    try:
        xml = converter.convert(text, stop_on_error=not args.continue_on_error)

        # Write output file (unless --no-file is specified)
        if not args.no_file:
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(xml)
                print(f"Successfully converted to: {output_path}")
            except Exception as e:
                print(f"Error writing output file: {e}", file=sys.stderr)
                return 1

        # Copy to clipboard if requested
        if args.clipboard:
            try:
                from .fmclip import (
                    set_clipboard_fm_objects,
                    UnsupportedPlatformError,
                    InvalidXMLError,
                    FMClipError
                )

                set_clipboard_fm_objects(xml)
                print("✓ Copied to clipboard as FileMaker objects. Ready to paste into FileMaker Pro.")

            except UnsupportedPlatformError:
                print("Error: Clipboard functionality is only available on macOS.", file=sys.stderr)
                return 1
            except InvalidXMLError as e:
                print(f"Error: Invalid XML for FileMaker: {e}", file=sys.stderr)
                return 1
            except FMClipError as e:
                print(f"Error copying to clipboard: {e}", file=sys.stderr)
                return 1

        return 0

    except UnknownStepError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main())

