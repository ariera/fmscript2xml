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

    expected_steps = _extract_steps(expected_root)
    generated_steps = _extract_steps(generated_root)

    # If comparing Script/ObjectList expected XML against fmxmlsnippet output,
    # comment steps can be inconsistent between sources (sanitized input vs original XML).
    if expected_root.tag == "Script" and generated_root.tag == "fmxmlsnippet":
        expected_steps = _filter_comment_steps(expected_steps)
        generated_steps = _filter_comment_steps(generated_steps)

    result = ComparisonResult()

    if len(expected_steps) < len(generated_steps):
        for idx in range(len(expected_steps), len(generated_steps)):
            step = generated_steps[idx]
            result.extra_steps.append(_step_label(step, idx))
    elif len(expected_steps) > len(generated_steps):
        for idx in range(len(generated_steps), len(expected_steps)):
            step = expected_steps[idx]
            result.missing_steps.append(_step_label(step, idx))

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

    # Script/ObjectList steps include a hash attribute that shouldn't affect comparison
    expected.attrib.pop("hash", None)
    generated.attrib.pop("hash", None)

    remove_ids(expected, requires_db_ids=requires_db_ids)
    remove_ids(generated, requires_db_ids=requires_db_ids)
    normalize_whitespace(expected)
    normalize_whitespace(generated)
    sort_attributes(expected)
    sort_attributes(generated)

    diffs: List[str] = []

    expected_name = _normalize_step_name(expected.attrib.get("name", ""))
    generated_name = _normalize_step_name(generated.attrib.get("name", ""))

    if _is_script_step(expected):
        diffs.extend(_compare_script_step(expected, generated))
    else:
        # Compare core attributes
        for attr in ("name", "id", "enable"):
            expected_value = expected.attrib.get(attr)
            generated_value = generated.attrib.get(attr)
            if attr == "name":
                expected_value = expected_name
                generated_value = generated_name
            if expected_value != generated_value:
                diffs.append(
                    f"Attribute mismatch '{attr}': "
                    f"expected='{expected_value}' "
                    f"generated='{generated_value}'"
                )

        # Compare structure recursively
        _compare_elements(expected, generated, diffs, path="Step")

    return StepComparison(
        step_index=step_index,
        expected_name=expected_name,
        generated_name=generated_name,
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
        lines.append(
            f"Step {diff.step_index}: expected='{diff.expected_name}' "
            f"generated='{diff.generated_name}'"
        )
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
        diffs.append(
            f"{path}: text mismatch expected='{_shorten(expected.text)}' "
            f"generated='{_shorten(generated.text)}'"
        )

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


def _step_label(step: ET.Element, index: Optional[int] = None) -> str:
    name = _normalize_step_name(step.attrib.get("name", ""))
    label = f"{name} (id={step.attrib.get('id', '')})"
    if index is not None:
        return f"{index}: {label}"
    return label


def _safe_int(value: Optional[str]) -> Optional[int]:
    try:
        return int(value) if value is not None else None
    except ValueError:
        return None


def _shorten(text: Optional[str], limit: int = 160) -> str:
    if text is None:
        return ""
    if len(text) <= limit:
        return text
    return f"{text[:limit]}…"


def _extract_steps(root: ET.Element) -> List[ET.Element]:
    """Extract Step elements in order for different XML shapes."""
    # fmxmlsnippet format: Steps are direct children
    if root.tag == "fmxmlsnippet":
        return [e for e in list(root) if e.tag == "Step"]

    # Script format: Steps are under ObjectList
    object_list = root.find("ObjectList")
    if object_list is not None:
        return [e for e in list(object_list) if e.tag == "Step"]

    # Fallback: collect all Step elements in document order
    return list(root.findall(".//Step"))


def _normalize_step_name(name: str) -> str:
    """Normalize step names across Script/ObjectList and fmxmlsnippet formats."""
    if name == "# (comment)":
        return "Comment"
    return name


def _filter_comment_steps(steps: List[ET.Element]) -> List[ET.Element]:
    """Remove Comment steps from a list."""
    filtered: List[ET.Element] = []
    for step in steps:
        if _normalize_step_name(step.attrib.get("name", "")) == "Comment":
            continue
        filtered.append(step)
    return filtered


def _is_script_step(step: ET.Element) -> bool:
    """Detect Script/ObjectList-style steps with ParameterValues."""
    return step.find("ParameterValues") is not None or step.find("Options") is not None


def _compare_script_step(expected: ET.Element, generated: ET.Element) -> List[str]:
    """Compare Script/ObjectList step against fmxmlsnippet step."""
    diffs: List[str] = []

    # Ignore hash attribute from Script/ObjectList steps
    expected.attrib.pop("hash", None)

    for attr in ("name", "id", "enable"):
        expected_value = expected.attrib.get(attr)
        generated_value = generated.attrib.get(attr)
        if attr == "name":
            expected_value = _normalize_step_name(expected_value or "")
            generated_value = _normalize_step_name(generated_value or "")
        if expected_value != generated_value:
            diffs.append(
                f"Attribute mismatch '{attr}': "
                f"expected='{expected_value}' "
                f"generated='{generated_value}'"
            )

    # Compare FieldReference name against generated Field name when present
    expected_field = expected.find(".//Parameter[@type='FieldReference']//FieldReference")
    generated_field = generated.find("Field")
    if expected_field is not None and generated_field is not None:
        expected_field_name = expected_field.attrib.get("name")
        expected_table = expected_field.find("TableOccurrenceReference")
        if expected_table is not None:
            table_name = expected_table.attrib.get("name")
            if table_name and expected_field_name:
                expected_field_name = f"{table_name}::{expected_field_name}"
        generated_field_name = generated_field.attrib.get("name")
        # If expected field name is missing but the table is marked as missing,
        # tolerate broken reference placeholders in generated output.
        if not expected_field_name and expected_table is not None:
            table_name = expected_table.attrib.get("name") or ""
            if "Table Missing" in table_name or "Table Missing" in (generated_field_name or "") or "BROKEN REFERENCE" in (generated_field_name or ""):
                expected_field_name = generated_field_name
        if expected_field_name != generated_field_name:
            diffs.append(
                f"Field name mismatch expected='{expected_field_name}' "
                f"generated='{generated_field_name}'"
            )

    # Compare Calculation text when present
    expected_calc = expected.find(".//Parameter[@type='Calculation']//Text")
    generated_calc = generated.find(".//Interval/Calculation")
    if generated_calc is None:
        generated_calc = generated.find(".//Calculation")
    if expected_calc is not None and generated_calc is not None:
        expected_text = (expected_calc.text or "").strip()
        generated_text = (generated_calc.text or "").strip()
        if expected_text != generated_text:
            diffs.append(
                f"Calculation mismatch expected='{_shorten(expected_text)}' "
                f"generated='{_shorten(generated_text)}'"
            )

    # Compare ScriptReference name when present
    expected_script = expected.find(".//Parameter[@type='ScriptReference']//ScriptReference")
    generated_script = generated.find("Script")
    if expected_script is not None and generated_script is not None:
        expected_name = expected_script.attrib.get("name")
        generated_name = generated_script.attrib.get("name")
        if expected_name != generated_name:
            diffs.append(
                f"Script name mismatch expected='{expected_name}' "
                f"generated='{generated_name}'"
            )

    return diffs
