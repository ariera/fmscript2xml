"""FileMaker Script to XML Parser"""

__version__ = "0.3.8"

from .converter import Converter, UnknownStepError
from .fmclip import (
    set_clipboard_fm_objects,
    get_clipboard_fm_objects_as_xml,
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
    'clipboard_has_fm_objects',
    'validate_fm_xml',
    'FMClipError',
    'UnsupportedPlatformError',
    'InvalidXMLError',
]

