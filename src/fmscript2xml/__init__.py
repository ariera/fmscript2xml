"""FileMaker Script to XML Parser.

Discontinued: replaced by the fmscript2xml macOS app,
https://github.com/ariera/fmscript2xml-app
"""

__version__ = "0.5.4"

from .converter import Converter, UnknownStepError
from .fmclip import (
    set_clipboard_fm_objects,
    get_clipboard_fm_objects_as_xml,
    get_clipboard_text,
    clipboard_has_fm_objects,
    validate_fm_xml,
    FMClipError,
    UnsupportedPlatformError,
    InvalidXMLError,
)

__all__ = [
    'Converter',
    'UnknownStepError',
    'set_clipboard_fm_objects',
    'get_clipboard_fm_objects_as_xml',
    'get_clipboard_text',
    'clipboard_has_fm_objects',
    'validate_fm_xml',
    'FMClipError',
    'UnsupportedPlatformError',
    'InvalidXMLError',
]

