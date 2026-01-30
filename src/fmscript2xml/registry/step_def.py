"""
Data classes for step definitions.

Represents the structure of FileMaker script step definitions
loaded from markdown files.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


@dataclass
class ConditionalElement:
    """Represents a conditional XML element."""

    element_name: str
    condition: str
    description: str = ""


@dataclass
class MappingRule:
    """Represents a mapping rule for converting parameters to XML."""

    rule_type: str  # e.g., "field", "calculation", "layout"
    source_param: Optional[str] = None  # Parameter name in input
    target_element: Optional[str] = None  # XML element name
    target_attribute: Optional[str] = None  # XML attribute name
    requires_cdata: bool = False
    omit_id: bool = False  # Whether to omit database-specific ID


@dataclass
class XMLTemplate:
    """Template for XML structure of a step."""

    structure: str  # XML structure template
    examples: List[str] = field(default_factory=list)


@dataclass
class StepDefinition:
    """Complete definition of a FileMaker script step."""

    id: int
    name: str
    category: str
    status: str = "draft"  # draft | stable | deprecated
    input_patterns: List[str] = field(default_factory=list)
    fm_name: str = ""
    enable_default: bool = True
    wrapper: str = "step-only"  # step-only | with-snippet

    # XML generation info
    xml_step_name: str = ""
    mapping_rules: List[MappingRule] = field(default_factory=list)
    conditional_elements: List[ConditionalElement] = field(default_factory=list)
    xml_template: Optional[XMLTemplate] = None

    # Policy flags
    requires_db_ids: bool = False  # Whether step references database-specific IDs

    # Raw data from markdown
    description: str = ""
    examples: List[Dict[str, str]] = field(default_factory=list)  # List of {input, output} dicts

    def __post_init__(self):
        """Set defaults after initialization."""
        if not self.xml_step_name:
            self.xml_step_name = self.name
        if not self.fm_name:
            self.fm_name = self.name

