"""
FileMaker clipboard utilities.

Converts XML to FileMaker's native clipboard format using macOS AppleScript.
This allows pasting script steps directly into FileMaker Pro.

macOS only - requires osascript.
"""

import subprocess
import tempfile
import os
import platform
import re
from typing import Optional, Tuple


# FileMaker clipboard type codes
FM_OBJECT_CODES = {
    'Step': 'XMSS',      # Script steps
    'Script': 'XMSC',    # Scripts (and script folders/groups)
    'Group': 'XMSC',     # Script groups (folders)
    'CustomFunction': 'XMFN',
    'Field': 'XMFD',
    'BaseTable': 'XMTB',
    'ValueList': 'XMVL',
    'Layout': 'XML2',    # FM12+ layout objects
}


class FMClipError(Exception):
    """Error related to FileMaker clipboard operations."""
    pass


class UnsupportedPlatformError(FMClipError):
    """Raised when trying to use clipboard on non-macOS platform."""
    pass


class InvalidXMLError(FMClipError):
    """Raised when XML is not valid for FileMaker."""
    pass


def is_macos() -> bool:
    """Check if running on macOS."""
    return platform.system() == 'Darwin'


def detect_fm_object_type(xml_string: str) -> Tuple[str, str]:
    """
    Detect the FileMaker object type from XML.

    Args:
        xml_string: XML string containing FileMaker objects

    Returns:
        Tuple of (object_name, object_code) e.g. ('Step', 'XMSS')

    Raises:
        InvalidXMLError: If XML doesn't contain valid FM objects
    """
    # Check for fmxmlsnippet wrapper
    if '<fmxmlsnippet' not in xml_string:
        raise InvalidXMLError("XML must be wrapped in <fmxmlsnippet> element")

    # Find the first element inside fmxmlsnippet
    # Pattern: <fmxmlsnippet...>...<ElementName
    match = re.search(
        r'<fmxmlsnippet[^>]*>\s*<(\w+)',
        xml_string,
        re.DOTALL
    )

    if not match:
        raise InvalidXMLError("Could not find FileMaker object element inside fmxmlsnippet")

    element_name = match.group(1)

    # Map element name to FM object code
    if element_name in FM_OBJECT_CODES:
        return element_name, FM_OBJECT_CODES[element_name]

    raise InvalidXMLError(
        f"Unknown FileMaker object type: '{element_name}'. "
        f"Expected one of: {', '.join(FM_OBJECT_CODES.keys())}"
    )


def validate_fm_xml(xml_string: str) -> bool:
    """
    Validate that XML is valid for FileMaker clipboard.

    Args:
        xml_string: XML string to validate

    Returns:
        True if valid

    Raises:
        InvalidXMLError: If XML is invalid
    """
    # Check basic structure
    if not xml_string.strip():
        raise InvalidXMLError("XML string is empty")

    # Check for fmxmlsnippet
    if '<fmxmlsnippet' not in xml_string:
        raise InvalidXMLError("XML must contain <fmxmlsnippet> element")

    if '</fmxmlsnippet>' not in xml_string:
        raise InvalidXMLError("XML must have closing </fmxmlsnippet> tag")

    # Check type attribute
    if 'type="FMObjectList"' not in xml_string and 'type="LayoutObjectList"' not in xml_string:
        raise InvalidXMLError(
            "fmxmlsnippet must have type=\"FMObjectList\" or type=\"LayoutObjectList\""
        )

    # Detect object type (this also validates structure)
    detect_fm_object_type(xml_string)

    return True


def set_clipboard_fm_objects(xml_string: str) -> bool:
    """
    Set macOS clipboard with FileMaker objects from XML string.

    Uses osascript to leverage macOS's native FileMaker data handlers.

    Args:
        xml_string: Valid FileMaker XML string

    Returns:
        True if successful

    Raises:
        UnsupportedPlatformError: If not running on macOS
        InvalidXMLError: If XML is not valid for FileMaker
        FMClipError: If clipboard operation fails
    """
    if not is_macos():
        raise UnsupportedPlatformError(
            "Clipboard functionality is only available on macOS"
        )

    # Validate XML
    validate_fm_xml(xml_string)

    # Detect object type
    obj_name, obj_code = detect_fm_object_type(xml_string)

    # Write XML to temp file
    temp_fd, temp_path = tempfile.mkstemp(suffix='.xml', prefix='fmscript_')
    try:
        with os.fdopen(temp_fd, 'w', encoding='utf-8') as f:
            f.write(xml_string)

        # Build AppleScript to convert XML to FM objects and set clipboard
        # The key is reading the file "as" the FM class, which triggers
        # macOS's registered handler to convert XML → FM binary format
        applescript = f'''
            set xmlFilePath to POSIX file "{temp_path}"
            try
                set fmObjects to read xmlFilePath as «class {obj_code}»
                set the clipboard to fmObjects
                return "success"
            on error errMsg number errNum
                return "error:" & errMsg
            end try
        '''

        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            error_msg = result.stderr.strip() or "Unknown error"
            raise FMClipError(f"AppleScript error: {error_msg}")

        output = result.stdout.strip()
        if output.startswith("error:"):
            raise FMClipError(f"FileMaker conversion error: {output[6:]}")

        return True

    finally:
        # Clean up temp file
        try:
            os.unlink(temp_path)
        except OSError:
            pass


def get_clipboard_fm_objects_as_xml() -> Optional[str]:
    """
    Get FileMaker objects from clipboard as XML string.

    Returns:
        XML string if clipboard contains FM objects, None otherwise

    Raises:
        UnsupportedPlatformError: If not running on macOS
    """
    if not is_macos():
        raise UnsupportedPlatformError(
            "Clipboard functionality is only available on macOS"
        )

    # Try each FM object type
    for obj_name, obj_code in FM_OBJECT_CODES.items():
        applescript = f'''
            try
                set fmObjects to the clipboard as «class {obj_code}»
                set tempFolder to (do shell script "mktemp -d") & "/"
                set tempFile to tempFolder & "clipboard.xml"
                set tempFilePath to POSIX file tempFile

                tell application "System Events"
                    set fileRef to open for access tempFilePath with write permission
                    write fmObjects to fileRef
                    close access fileRef
                end tell

                set xmlContent to read tempFilePath as «class utf8»
                do shell script "rm -rf " & quoted form of tempFolder
                return xmlContent
            on error
                return ""
            end try
        '''

        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True,
            text=True
        )

        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()

    return None


def clipboard_has_fm_objects() -> bool:
    """
    Check if clipboard contains FileMaker objects.

    Returns:
        True if clipboard contains FM objects

    Raises:
        UnsupportedPlatformError: If not running on macOS
    """
    if not is_macos():
        raise UnsupportedPlatformError(
            "Clipboard functionality is only available on macOS"
        )

    # Check for any FM object type in clipboard
    for obj_code in FM_OBJECT_CODES.values():
        applescript = f'''
            try
                set fmObjects to the clipboard as «class {obj_code}»
                return "found"
            on error
                return ""
            end try
        '''

        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True,
            text=True
        )

        if result.returncode == 0 and result.stdout.strip() == "found":
            return True

    return False
