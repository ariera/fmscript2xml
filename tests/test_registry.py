"""Tests for registry module."""

import pytest
from pathlib import Path
from fmscript2xml.registry.loader import StepRegistry


class TestStepRegistry:
    """Test step registry functionality."""

    def test_load_registry(self):
        """Test loading step definitions from JSON."""
        registry = StepRegistry()

        # Should have loaded steps
        assert len(registry.all_steps()) > 0
        # Should have at least 166 steps (might have obsolete ones)
        assert len(registry.all_steps()) >= 166

    def test_get_step_by_name(self):
        """Test getting step by name."""
        registry = StepRegistry()

        # Try to get a known step
        step_def = registry.get("Set Variable")
        assert step_def is not None
        assert step_def['name'] == "Set Variable"
        assert step_def['id'] == 141
        assert 'xml_step_name' in step_def
        assert 'enable_default' in step_def

    def test_get_step_by_id(self):
        """Test getting step by ID."""
        registry = StepRegistry()

        # Try to get step by ID
        step_def = registry.get_by_id(141)
        assert step_def is not None
        assert step_def['id'] == 141
        assert step_def['name'] == "Set Variable"

    def test_step_names(self):
        """Test getting all step names."""
        registry = StepRegistry()

        names = registry.step_names()
        assert len(names) > 0
        assert "Set Variable" in names
        assert "If" in names

    def test_unknown_step(self):
        """Test getting unknown step returns None."""
        registry = StepRegistry()

        step_def = registry.get("Unknown Step That Does Not Exist")
        assert step_def is None

    def test_step_definition_structure(self):
        """Test that step definitions have required fields."""
        registry = StepRegistry()

        # Get a few known steps
        for step_name in ["Set Variable", "If", "End If"]:
            step_def = registry.get(step_name)
            assert step_def is not None, f"Step {step_name} should exist"

            # Check required fields
            assert 'id' in step_def
            assert 'name' in step_def
            assert 'xml_step_name' in step_def
            assert 'enable_default' in step_def

            # Check field types
            assert isinstance(step_def['id'], int)
            assert isinstance(step_def['name'], str)
            assert isinstance(step_def['xml_step_name'], str)
            assert isinstance(step_def['enable_default'], bool)
