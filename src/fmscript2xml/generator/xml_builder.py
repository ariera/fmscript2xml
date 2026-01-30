"""
XML construction utilities for FileMaker script steps.

Handles:
- Building Step elements with correct attributes
- CDATA wrapping for calculations
- Database ID omission policy
- Helper comment generation
"""

from xml.etree import ElementTree as ET
from typing import Optional, Dict, Any, List
from xml.dom import minidom


def create_step_element(
    step_id: int,
    step_name: str,
    enabled: bool = True
) -> ET.Element:
    """
    Create a Step element with standard attributes.

    Args:
        step_id: Step ID
        step_name: Step name
        enabled: Whether step is enabled

    Returns:
        ET.Element for the Step
    """
    step = ET.Element('Step')
    step.set('enable', 'True' if enabled else 'False')
    step.set('id', str(step_id))
    step.set('name', step_name)
    return step


def create_cdata_element(text: str) -> ET.Element:
    """
    Create a Calculation element with CDATA content.

    Args:
        text: Calculation text

    Returns:
        ET.Element with Calculation containing CDATA
    """
    calc = ET.Element('Calculation')
    # Use CDATA section
    calc.text = text
    # Note: ElementTree doesn't support CDATA directly, but we'll format it
    # in the final output. For now, just set the text.
    return calc


def create_text_element(element_name: str, text: str) -> ET.Element:
    """
    Create a simple text element.

    Args:
        element_name: Element name
        text: Text content

    Returns:
        ET.Element
    """
    elem = ET.Element(element_name)
    elem.text = text
    return elem


def create_field_element(
    field_name: str,
    table_name: Optional[str] = None,
    repetition: Optional[str] = None,
    omit_id: bool = True
) -> ET.Element:
    """
    Create a Field element, omitting ID per policy.

    Args:
        field_name: Field name
        table_name: Table name (optional)
        repetition: Repetition number (optional)
        omit_id: Whether to omit ID attribute (default: True)

    Returns:
        ET.Element for Field
    """
    field = ET.Element('Field')
    field.set('name', field_name)

    if table_name:
        field.set('table', table_name)

    if repetition:
        field.set('repetition', str(repetition))

    # Never set ID per policy
    return field


def create_layout_element(
    layout_name: str,
    omit_id: bool = True
) -> ET.Element:
    """
    Create a Layout element, omitting ID per policy.

    Args:
        layout_name: Layout name
        omit_id: Whether to omit ID attribute (default: True)

    Returns:
        ET.Element for Layout
    """
    layout = ET.Element('Layout')
    layout.set('name', layout_name)
    # Never set ID per policy
    return layout


def create_table_element(
    table_name: str,
    omit_id: bool = True
) -> ET.Element:
    """
    Create a Table element, omitting ID per policy.

    Args:
        table_name: Table name
        omit_id: Whether to omit ID attribute (default: True)

    Returns:
        ET.Element for Table
    """
    table = ET.Element('Table')
    table.set('name', table_name)
    # Never set ID per policy
    return table


def create_comment_step(comment_text: str) -> ET.Element:
    """
    Create a Comment step element.

    Args:
        comment_text: Comment text

    Returns:
        ET.Element for Comment step
    """
    step = create_step_element(89, 'Comment')
    text_elem = create_text_element('Text', comment_text)
    step.append(text_elem)
    return step


def create_helper_comment_step(original_text: str) -> ET.Element:
    """
    Create a helper comment step for manual reference.

    Used when a step requires database-specific IDs that cannot be resolved.

    Args:
        original_text: Original plain text script step

    Returns:
        ET.Element for Comment step with helper text
    """
    helper_text = f"Original: {original_text}"
    return create_comment_step(helper_text)


def format_xml_with_cdata(root: ET.Element) -> str:
    """
    Format XML with proper CDATA sections.

    ElementTree doesn't support CDATA directly, so we format it manually.
    CDATA sections preserve content exactly, including & characters.

    Args:
        root: Root element

    Returns:
        Formatted XML string with CDATA
    """
    # Convert to string first
    # Use method='c14n' or manually handle to avoid escaping in CDATA
    rough_string = ET.tostring(root, encoding='unicode', method='xml')

    # Replace Calculation text with CDATA
    # Need to unescape entities that were escaped by ElementTree
    import re
    import html

    # Pattern: <Calculation>text</Calculation>
    def replace_calc(match):
        calc_text = match.group(1)
        # Unescape XML entities (ElementTree escapes & to &amp;)
        # But in CDATA, we want the original characters
        calc_text = html.unescape(calc_text)
        # Always use CDATA for calculations
        return f'<Calculation><![CDATA[{calc_text}]]></Calculation>'

    rough_string = re.sub(
        r'<Calculation>(.*?)</Calculation>',
        replace_calc,
        rough_string,
        flags=re.DOTALL
    )

    # Pretty print
    try:
        dom = minidom.parseString(rough_string)
        return dom.toprettyxml(indent='  ')
    except Exception:
        # Fallback to simple formatting
        return rough_string


def create_fmxmlsnippet(steps: List[ET.Element]) -> ET.Element:
    """
    Create fmxmlsnippet wrapper with list of steps.

    Args:
        steps: List of Step elements

    Returns:
        ET.Element for fmxmlsnippet
    """
    root = ET.Element('fmxmlsnippet')
    root.set('type', 'FMObjectList')

    for step in steps:
        root.append(step)

    return root


def to_xml_string(root: ET.Element, pretty: bool = True) -> str:
    """
    Convert element tree to XML string.

    Args:
        root: Root element
        pretty: Whether to pretty-print

    Returns:
        XML string
    """
    if pretty:
        return format_xml_with_cdata(root)
    else:
        return ET.tostring(root, encoding='unicode')

