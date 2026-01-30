"""
Example usage of fmscript2xml converter.

This demonstrates how to use the converter programmatically.
"""

from pathlib import Path
from fmscript2xml import Converter


def example_basic_usage():
    """Basic usage example."""
    # Create converter
    converter = Converter()

    # Convert a simple script
    script = """
    Set Variable [ $counter ; Value: 0 ]
    If [ $counter < 10 ]
        Set Variable [ $counter ; Value: $counter + 1 ]
    End If
    """

    xml = converter.convert(script)
    print("Generated XML:")
    print(xml)


def example_with_comments():
    """Example with comments."""
    converter = Converter()

    script = """
    # Initialize counter
    Set Variable [ $counter ; Value: 0 ]

    # Loop until done
    If [ $counter < 10 ]
        Set Variable [ $counter ; Value: $counter + 1 ]
    End If
    """

    xml = converter.convert(script)
    print(xml)


def example_validation():
    """Example of validation."""
    converter = Converter()

    script = "Set Variable [ $var ; Value: 1 ]"

    is_valid, errors = converter.validate(script)
    if is_valid:
        print("Script is valid!")
    else:
        print("Script has errors:")
        for error in errors:
            print(f"  - {error}")


def example_error_handling():
    """Example of error handling."""
    converter = Converter()

    script = """
    Set Variable [ $var ; Value: 1 ]
    Unknown Step [ param: value ]
    Exit Script
    """

    try:
        # Stop on first error
        xml = converter.convert(script, stop_on_error=True)
    except Exception as e:
        print(f"Error: {e}")

    # Or continue processing
    xml = converter.convert(script, stop_on_error=False)
    print("XML with errors:")
    print(xml)


if __name__ == '__main__':
    print("=== Basic Usage ===")
    example_basic_usage()

    print("\n=== With Comments ===")
    example_with_comments()

    print("\n=== Validation ===")
    example_validation()

    print("\n=== Error Handling ===")
    example_error_handling()

