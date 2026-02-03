"""
Step-specific XML generation handlers.

This module provides the main entry point for generating XML from parsed steps.
Individual handlers are organized in the handlers/ subdirectory.
"""

from typing import List, Optional
from xml.etree import ElementTree as ET
from ..parser.parser import ParsedStep
from .xml_builder import create_step_element, create_cdata_element
from .handlers import HANDLERS, StepHandler


def get_handler(step_name: str) -> Optional[StepHandler]:
    """Get handler for step name."""
    return HANDLERS.get(step_name)


def generate_xml(
    step: ParsedStep,
    step_def: dict
) -> List[ET.Element]:
    """
    Generate XML for a parsed step using appropriate handler.

    Args:
        step: Parsed step
        step_def: Step definition dict with keys: id, name, xml_step_name, enable_default

    Returns:
        List of XML elements (may include helper comments)
    """
    # Try to find specific handler
    handler = get_handler(step.name)

    if handler and handler.can_handle(step, step_def):
        return handler.generate(step, step_def)

    # Default handler: create basic step element
    # Check if step is disabled (// prefix)
    enabled = step_def['enable_default'] and not step.is_disabled
    step_elem = create_step_element(
        step_def['id'],
        step_def['xml_step_name'],
        enabled
    )

    # Add parameters as child elements (generic handling)
    for key, value in step.params.items():
        if key.isdigit():
            # Positional parameter - treat as calculation
            calc_elem = create_cdata_element(str(value))
            step_elem.append(calc_elem)
        else:
            # Named parameter - sanitize element name (XML element names cannot contain spaces)
            # Replace spaces with camelCase or remove them
            element_name = key.replace(' ', '')  # Simple approach: remove spaces
            # If empty after removing spaces, use a default name
            if not element_name:
                element_name = 'Parameter'
            param_elem = ET.Element(element_name)
            param_elem.text = str(value)
            step_elem.append(param_elem)

    return [step_elem]
