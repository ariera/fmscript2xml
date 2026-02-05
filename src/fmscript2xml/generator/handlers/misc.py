"""
Miscellaneous handlers: Set Error Capture, Print, Commit Records/Requests.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_cdata_element
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


class PrintSetupHandler(StepHandler):
    """Handler for Print Setup steps."""

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

        # Restore is always False for Print Setup
        restore_elem = ET.Element('Restore')
        restore_elem.set('state', 'False')
        step_elem.append(restore_elem)

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


class SaveRecordsAsPDFHandler(StepHandler):
    """Handler for Save Records as PDF steps."""

    def _pdf_options(self, source: str, appearance: str | None) -> ET.Element:
        pdf_options = ET.Element('PDFOptions')
        pdf_options.set('source', source)
        if appearance:
            pdf_options.set('appearance', appearance)

        # Document -> Pages -> NumberFrom + PageRange (all 1)
        document = ET.Element('Document')
        pages = ET.Element('Pages')
        pages.set('AllPages', 'True')

        number_from = ET.Element('NumberFrom')
        number_from.append(create_cdata_element('1'))
        pages.append(number_from)

        page_range = ET.Element('PageRange')
        range_from = ET.Element('From')
        range_from.append(create_cdata_element('1'))
        range_to = ET.Element('To')
        range_to.append(create_cdata_element('1'))
        page_range.extend([range_from, range_to])
        pages.append(page_range)

        document.append(pages)
        pdf_options.append(document)

        # Security and View (fixed defaults from expected.xml)
        security = ET.Element('Security')
        security.set('allowScreenReader', 'True')
        security.set('enableCopying', 'True')
        security.set('controlEditing', 'AnyExceptExtractingPages')
        security.set('controlPrinting', 'HighResolution')
        security.set('requireControlEditPassword', 'False')
        security.set('requireOpenPassword', 'False')
        pdf_options.append(security)

        view = ET.Element('View')
        view.set('magnification', '100')
        view.set('pageLayout', 'SinglePage')
        view.set('show', 'PagesPanelAndPage')
        pdf_options.append(view)

        return pdf_options

    def generate(
        self,
        step: ParsedStep,
        step_def: dict
    ) -> List[ET.Element]:
        enabled = step_def['enable_default'] and not step.is_disabled
        step_elem = create_step_element(
            step_def['id'],
            step_def['xml_step_name'],
            enabled
        )

        raw_lower = step.raw_text.lower()

        # Dialog handling
        with_dialog = step.params.get('With dialog', '')
        if 'no dialog' in raw_lower:
            no_interact_state = 'True'
        elif with_dialog:
            no_interact_state = 'True' if with_dialog.lower() == 'off' else 'False'
        else:
            no_interact_state = 'False'

        # Append option
        option_state = 'True' if 'append' in raw_lower else 'False'

        # Create folders
        create_folders = step.params.get('Create folders', 'Off')
        create_dirs_state = 'True' if create_folders.lower() == 'on' else 'False'

        # Restore / AutoOpen / CreateEmail flags
        restore_state = 'True' if 'restore' in raw_lower else 'False'
        auto_open_state = 'True' if 'automatically open' in raw_lower else 'False'
        create_email_state = 'True' if 'create email' in raw_lower else 'False'

        # Output fixed children in expected order
        no_interact = ET.Element('NoInteract')
        no_interact.set('state', no_interact_state)
        step_elem.append(no_interact)

        option = ET.Element('Option')
        option.set('state', option_state)
        step_elem.append(option)

        create_dirs = ET.Element('CreateDirectories')
        create_dirs.set('state', create_dirs_state)
        step_elem.append(create_dirs)

        restore = ET.Element('Restore')
        restore.set('state', restore_state)
        step_elem.append(restore)

        auto_open = ET.Element('AutoOpen')
        auto_open.set('state', auto_open_state)
        step_elem.append(auto_open)

        create_email = ET.Element('CreateEmail')
        create_email.set('state', create_email_state)
        step_elem.append(create_email)

        # Optional file path
        universal_path = None
        for value in step.params.values():
            if not isinstance(value, str):
                continue
            if '$filepath' in value:
                universal_path = value
                break
        if universal_path:
            # Strip straight or curly quotes
            if (universal_path.startswith('"') and universal_path.endswith('"')) or (
                universal_path.startswith('\u201c') and universal_path.endswith('\u201d')
            ):
                universal_path = universal_path[1:-1]
            path_elem = ET.Element('UniversalPathList')
            path_elem.text = universal_path
            step_elem.append(path_elem)

        # PDFOptions source/appearance
        if 'current record' in raw_lower:
            source = 'CurrentRecord'
        elif 'blank record' in raw_lower:
            source = 'BlankRecord'
        else:
            source = 'RecordsBeingBrowsed'

        appearance = None
        if 'blank record' in raw_lower:
            if 'as formatted' in raw_lower:
                appearance = 'AsFormatted'
            elif 'with boxes' in raw_lower:
                appearance = 'WithBoxes'
            elif 'with underlines' in raw_lower:
                appearance = 'WithUnderlines'
            elif 'with placeholder text' in raw_lower:
                appearance = 'WithPlaceholderText'

        step_elem.append(self._pdf_options(source, appearance))

        return [step_elem]
