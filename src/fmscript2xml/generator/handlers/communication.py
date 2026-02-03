"""
Handlers for communication steps: Open URL, Send Mail.
"""

from typing import List
from xml.etree import ElementTree as ET
from ...parser.parser import ParsedStep
from ..xml_builder import create_step_element, create_cdata_element
from .base import StepHandler


class OpenURLHandler(StepHandler):
    """Handler for Open URL steps."""

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

        # NoInteract element for "With dialog" option
        # "With dialog: Off" -> NoInteract state="True"
        # "With dialog: On" -> NoInteract state="False"
        with_dialog = step.params.get('With dialog', 'On')
        no_interact = ET.Element('NoInteract')
        no_interact.set('state', 'True' if with_dialog.lower() == 'off' else 'False')
        step_elem.append(no_interact)

        # URL calculation - get the positional parameter (the URL expression)
        url = step.params.get('0', '')
        if url:
            calc_elem = create_cdata_element(url)
            step_elem.append(calc_elem)

        return [step_elem]


class SendMailHandler(StepHandler):
    """Handler for Send Mail steps."""

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

        # NoInteract element for "With dialog" option
        with_dialog = step.params.get('With dialog', 'On')
        no_interact = ET.Element('NoInteract')
        no_interact.set('state', 'True' if with_dialog.lower() == 'off' else 'False')
        step_elem.append(no_interact)

        # To field
        to_value = step.params.get('To', '')
        if to_value:
            to_elem = ET.Element('To')
            to_elem.set('UseFoundSet', 'False')
            calc_elem = create_cdata_element(to_value)
            to_elem.append(calc_elem)
            step_elem.append(to_elem)

        # CC field
        cc_value = step.params.get('CC', step.params.get('Cc', ''))
        if cc_value:
            cc_elem = ET.Element('Cc')
            cc_elem.set('UseFoundSet', 'False')
            calc_elem = create_cdata_element(cc_value)
            cc_elem.append(calc_elem)
            step_elem.append(cc_elem)

        # BCC field
        bcc_value = step.params.get('BCC', step.params.get('Bcc', ''))
        if bcc_value:
            bcc_elem = ET.Element('Bcc')
            bcc_elem.set('UseFoundSet', 'False')
            calc_elem = create_cdata_element(bcc_value)
            bcc_elem.append(calc_elem)
            step_elem.append(bcc_elem)

        # Subject field
        subject_value = step.params.get('Subject', '')
        if subject_value:
            subject_elem = ET.Element('Subject')
            calc_elem = create_cdata_element(subject_value)
            subject_elem.append(calc_elem)
            step_elem.append(subject_elem)

        # Message field
        message_value = step.params.get('Message', '')
        if message_value:
            message_elem = ET.Element('Message')
            calc_elem = create_cdata_element(message_value)
            message_elem.append(calc_elem)
            step_elem.append(message_elem)

        # MultipleEmails - default to False
        multiple_emails = ET.Element('MultipleEmails')
        multiple_emails.set('state', 'False')
        step_elem.append(multiple_emails)

        # SendViaSMTP - check if "Send via E-mail Client" or "Send via SMTP"
        # First positional param often indicates the send method
        send_method = step.params.get('0', '')
        send_via_smtp = ET.Element('SendViaSMTP')
        send_via_smtp.set('state', 'True' if 'smtp' in send_method.lower() else 'False')
        step_elem.append(send_via_smtp)

        # SMTP Encryption type - default
        smtp_encryption = ET.Element('SMTPEncryptionType')
        smtp_encryption.set('type', 'SMTPEncryptionNone')
        step_elem.append(smtp_encryption)

        # SMTP Authentication type - default
        smtp_auth = ET.Element('SMTPAuthenticationType')
        smtp_auth.set('type', 'SMTPAuthenticationNone')
        step_elem.append(smtp_auth)

        return [step_elem]
