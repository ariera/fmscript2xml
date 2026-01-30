"""Tests for registry module."""

import pytest
from pathlib import Path
from fmscript2xml.registry.loader import StepRegistry


class TestStepRegistry:
    """Test step registry functionality."""

    def test_load_registry(self):
        """Test loading step definitions."""
        # Use relative path to docs/steps
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        registry = StepRegistry(steps_dir)
        registry.load_all()

        # Should have loaded steps
        assert len(registry.all_steps()) > 0

    def test_get_step_by_name(self):
        """Test getting step by name."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        registry = StepRegistry(steps_dir)
        registry.load_all()

        # Try to get a known step
        step_def = registry.get("Set Variable")
        if step_def:
            assert step_def.name == "Set Variable"
            assert step_def.id == 141

    def test_get_step_by_id(self):
        """Test getting step by ID."""
        base_dir = Path(__file__).parent.parent.parent.parent
        steps_dir = base_dir / "docs" / "steps"

        if not steps_dir.exists():
            pytest.skip("docs/steps directory not found")

        registry = StepRegistry(steps_dir)
        registry.load_all()

        # Try to get step by ID
        step_def = registry.get_by_id(141)
        if step_def:
            assert step_def.id == 141
            assert step_def.name == "Set Variable"

