"""XML normalization utilities for semantic comparison tests."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from typing import Optional


_DB_ID_TAGS = {"Layout", "Field", "Table"}


def normalize_xml(xml_string: str, requires_db_ids: bool = True) -> str:
    """
    Normalize XML for comparison.

    Args:
        xml_string: XML string to normalize
        requires_db_ids: If False, remove database-specific id attributes
    """
    root = ET.fromstring(xml_string)

    remove_helper_comments(root)
    remove_platform_data(root)
    remove_ids(root, requires_db_ids=requires_db_ids)
    normalize_whitespace(root)
    sort_attributes(root)

    return ET.tostring(root, encoding="unicode")


def remove_ids(element: ET.Element, requires_db_ids: bool) -> None:
    """
    Remove database-specific id attributes unless required.

    If requires_db_ids is False, remove id attributes from known DB-bound tags,
    and from any non-Step elements to avoid false mismatches.
    """
    for elem in element.iter():
        if requires_db_ids:
            continue
        if elem.tag == "Step":
            continue
        if "id" in elem.attrib and (elem.tag in _DB_ID_TAGS or elem.tag != "Step"):
            elem.attrib.pop("id", None)


def remove_helper_comments(root: ET.Element) -> None:
    """Remove helper comment steps that begin with 'Original:'."""
    to_remove = []
    for step in list(root):
        if step.tag != "Step":
            continue
        if step.attrib.get("name") != "Comment":
            continue
        text_elem = step.find("Text")
        if text_elem is None:
            continue
        if (text_elem.text or "").strip().startswith("Original:"):
            to_remove.append(step)
    for step in to_remove:
        root.remove(step)


def remove_platform_data(root: ET.Element) -> None:
    """Remove platform-specific data blocks (e.g., Print settings PlatformData)."""
    for elem in list(root.iter()):
        for child in list(elem):
            if child.tag == "PlatformData":
                elem.remove(child)


def normalize_whitespace(root: ET.Element) -> None:
    """Normalize whitespace in text and tail nodes."""
    for elem in root.iter():
        if elem.text:
            elem.text = _normalize_text(elem.text)
        if elem.tail:
            elem.tail = _normalize_text(elem.tail)


def _normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def sort_attributes(root: ET.Element) -> None:
    """Sort attributes on all elements for deterministic serialization."""
    for elem in root.iter():
        if elem.attrib:
            elem.attrib = dict(sorted(elem.attrib.items()))
