"""
Miscellaneous handlers: Set Error Capture, Print, Commit Records/Requests.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element
from .base import StepHandler


class SetErrorCaptureHandler(StepHandler):
    """Handler for Set Error Capture steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # Get the state from params - "On" or "Off"
        state_value = step.params.get('0', 'On')
        if not state_value:
            state_value = 'On'  # Default to On

        # Convert "On"/"Off" to "True"/"False"
        state = 'True' if state_value.lower() == 'on' else 'False'

        # Use <Set state="True/False"/> structure
        set_elem = ET.Element('Set')
        set_elem.set('state', state)
        step_elem.append(set_elem)

        return [step_elem]


class PrintHandler(StepHandler):
    """Handler for Print steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # NoInteract - "With dialog: On/Off" -> state="False/True"
        with_dialog = step.params.get('With dialog', 'On')
        no_interact_state = 'True' if with_dialog.lower() == 'off' else 'False'

        no_interact_elem = ET.Element('NoInteract')
        no_interact_elem.set('state', no_interact_state)
        step_elem.append(no_interact_elem)

        # Restore state - if "Restore" is present, state is True
        restore_value = step.params.get('Restore', '')
        restore_state = 'True' if restore_value else 'False'

        restore_elem = ET.Element('Restore')
        restore_elem.set('state', restore_state)
        step_elem.append(restore_elem)

        # Note: PrintSettings with PlatformData cannot be generated from text
        # FileMaker will use default print settings when pasted

        return [step_elem]


class CommitRecordsRequestsHandler(StepHandler):
    """Handler for Commit Records/Requests steps."""

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        # Check if step is disabled (// prefix)
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        # NoInteract - "With dialog: On/Off" or "No dialog" -> state="False/True"
        with_dialog = step.params.get('With dialog', '')
        no_dialog = step.params.get('0', '')

        # "No dialog" means no interaction (NoInteract=True)
        # "With dialog: Off" means no interaction (NoInteract=True)
        # "With dialog: On" means with interaction (NoInteract=False)
        if 'no dialog' in no_dialog.lower():
            no_interact_state = 'True'
        elif with_dialog:
            no_interact_state = 'True' if with_dialog.lower() == 'off' else 'False'
        else:
            no_interact_state = 'False'  # Default

        no_interact_elem = ET.Element('NoInteract')
        no_interact_elem.set('state', no_interact_state)
        step_elem.append(no_interact_elem)

        # Check for "Force Commit" option
        force_commit = 'force' in no_dialog.lower() if no_dialog else False

        # Option - always include, state depends on force commit
        option_elem = ET.Element('Option')
        option_elem.set('state', 'True' if force_commit else 'False')
        step_elem.append(option_elem)

        # ESSForceCommit - always include
        ess_elem = ET.Element('ESSForceCommit')
        ess_elem.set('state', 'True' if force_commit else 'False')
        step_elem.append(ess_elem)

        return [step_elem]
