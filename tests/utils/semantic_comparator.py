"""Semantic XML comparator for FileMaker step XML."""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import xml.etree.ElementTree as ET

from .xml_normalizer import (
    remove_helper_comments,
    remove_platform_data,
    remove_ids,
    normalize_whitespace,
    sort_attributes,
)


@dataclass
class StepComparison:
    step_index: int
    expected_name: str
    generated_name: str
    differences: List[str] = field(default_factory=list)


@dataclass
class ComparisonResult:
    missing_steps: List[str] = field(default_factory=list)
    extra_steps: List[str] = field(default_factory=list)
    step_differences: List[StepComparison] = field(default_factory=list)

    @property
    def is_equal(self) -> bool:
        return not (self.missing_steps or self.extra_steps or self.step_differences)


def compare_xml(
    expected_xml: str,
    generated_xml: str,
    ddr_ir: Optional[Dict[int, Dict]] = None
) -> ComparisonResult:
    """Compare two XML strings semantically."""
    expected_root = ET.fromstring(expected_xml)
    generated_root = ET.fromstring(generated_xml)

    remove_helper_comments(expected_root)
    remove_helper_comments(generated_root)
    remove_platform_data(expected_root)
    remove_platform_data(generated_root)
    normalize_whitespace(expected_root)
    normalize_whitespace(generated_root)
    sort_attributes(expected_root)
    sort_attributes(generated_root)

    expected_steps = [e for e in list(expected_root) if e.tag == "Step"]
    generated_steps = [e for e in list(generated_root) if e.tag == "Step"]

    result = ComparisonResult()

    if len(expected_steps) < len(generated_steps):
        for step in generated_steps[len(expected_steps):]:
            result.extra_steps.append(_step_label(step))
    elif len(expected_steps) > len(generated_steps):
        for step in expected_steps[len(generated_steps):]:
            result.missing_steps.append(_step_label(step))

    for idx in range(min(len(expected_steps), len(generated_steps))):
        expected_step = expected_steps[idx]
        generated_step = generated_steps[idx]

        step_info = None
        if ddr_ir is not None:
            step_id = _safe_int(expected_step.attrib.get("id"))
            if step_id is not None:
                step_info = ddr_ir.get(step_id)

        comparison = compare_steps(
            expected_step,
            generated_step,
            step_info=step_info,
            step_index=idx
        )
        if comparison.differences:
            result.step_differences.append(comparison)

    return result


def compare_steps(
    expected_step: ET.Element,
    generated_step: ET.Element,
    step_info: Optional[Dict] = None,
    step_index: int = 0
) -> StepComparison:
    """Compare two Step elements."""
    expected = deepcopy(expected_step)
    generated = deepcopy(generated_step)

    requires_db_ids = True
    if step_info is not None:
        requires_db_ids = step_info.get("requires_db_ids", True)

    remove_ids(expected, requires_db_ids=requires_db_ids)
    remove_ids(generated, requires_db_ids=requires_db_ids)
    normalize_whitespace(expected)
    normalize_whitespace(generated)
    sort_attributes(expected)
    sort_attributes(generated)

    diffs: List[str] = []

    # Compare core attributes
    for attr in ("name", "id", "enable"):
        if expected.attrib.get(attr) != generated.attrib.get(attr):
            diffs.append(
                f"Attribute mismatch '{attr}': "
                f"expected='{expected.attrib.get(attr)}' "
                f"generated='{generated.attrib.get(attr)}'"
            )

    # Compare structure recursively
    _compare_elements(expected, generated, diffs, path="Step")

    return StepComparison(
        step_index=step_index,
        expected_name=expected.attrib.get("name", ""),
        generated_name=generated.attrib.get("name", ""),
        differences=diffs
    )


def format_diff(result: ComparisonResult) -> str:
    """Render comparison result into a human-readable string."""
    lines: List[str] = []
    if result.missing_steps:
        lines.append("Missing steps:")
        lines.extend(f"  - {step}" for step in result.missing_steps)
    if result.extra_steps:
        lines.append("Extra steps:")
        lines.extend(f"  - {step}" for step in result.extra_steps)
    for diff in result.step_differences:
        lines.append(f"Step {diff.step_index}: {diff.expected_name}")
        lines.extend(f"  - {msg}" for msg in diff.differences)
    return "\n".join(lines)


def _compare_elements(
    expected: ET.Element,
    generated: ET.Element,
    diffs: List[str],
    path: str
) -> None:
    if expected.tag != generated.tag:
        diffs.append(f"{path}: tag mismatch expected='{expected.tag}' generated='{generated.tag}'")
        return

    if (expected.text or "") != (generated.text or ""):
        diffs.append(f"{path}: text mismatch expected='{expected.text}' generated='{generated.text}'")

    if expected.attrib != generated.attrib:
        diffs.append(f"{path}: attributes mismatch expected={expected.attrib} generated={generated.attrib}")

    expected_children = list(expected)
    generated_children = list(generated)

    if len(expected_children) != len(generated_children):
        diffs.append(
            f"{path}: child count mismatch expected={len(expected_children)} "
            f"generated={len(generated_children)}"
        )

    for idx in range(min(len(expected_children), len(generated_children))):
        child_path = f"{path}/{expected_children[idx].tag}[{idx}]"
        _compare_elements(expected_children[idx], generated_children[idx], diffs, child_path)


def _step_label(step: ET.Element) -> str:
    return f"{step.attrib.get('name', '')} (id={step.attrib.get('id', '')})"


def _safe_int(value: Optional[str]) -> Optional[int]:
    try:
        return int(value) if value is not None else None
    except ValueError:
        return None
