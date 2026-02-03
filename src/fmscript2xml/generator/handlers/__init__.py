"""
Step handler registry.

Exports all handlers and provides the HANDLERS registry.
"""

from .base import StepHandler
from .comment import CommentHandler
from .variable import SetVariableHandler
from .control import (
    IfHandler,
    ElseIfHandler,
    ElseHandler,
    EndIfHandler,
    ExitScriptHandler,
)
from .window import (
    NewWindowHandler,
    CloseWindowHandler,
    EnterPreviewModeHandler,
)
from .layout import (
    GoToLayoutHandler,
    GoToRecordRequestPageHandler,
    GoToRelatedRecordHandler,
)
from .field import (
    SetFieldHandler,
    SetFieldByNameHandler,
)
from .script import (
    PerformScriptHandler,
    InstallOnTimerScriptHandler,
)
from .find import PerformFindHandler
from .dialog import ShowCustomDialogHandler
from .communication import (
    OpenURLHandler,
    SendMailHandler,
)
from .misc import (
    PrintHandler,
    SetErrorCaptureHandler,
    CommitRecordsRequestsHandler,
)

# Registry of all handlers
HANDLERS = {
    'Comment': CommentHandler(),
    'Set Variable': SetVariableHandler(),
    'Set Error Capture': SetErrorCaptureHandler(),
    'New Window': NewWindowHandler(),
    'Close Window': CloseWindowHandler(),
    'Enter Preview Mode': EnterPreviewModeHandler(),
    'Print': PrintHandler(),
    'If': IfHandler(),
    'Else If': ElseIfHandler(),
    'Else': ElseHandler(),
    'End If': EndIfHandler(),
    'Exit Script': ExitScriptHandler(),
    'Perform Script': PerformScriptHandler(),
    'Go to Layout': GoToLayoutHandler(),
    'Go to Record/Request/Page': GoToRecordRequestPageHandler(),
    'Go to Related Record': GoToRelatedRecordHandler(),
    'Set Field': SetFieldHandler(),
    'Perform Find': PerformFindHandler(),
    'Show Custom Dialog': ShowCustomDialogHandler(),
    'Open URL': OpenURLHandler(),
    'Send Mail': SendMailHandler(),
    'Set Field By Name': SetFieldByNameHandler(),
    'Install OnTimer Script': InstallOnTimerScriptHandler(),
    'Commit Records/Requests': CommitRecordsRequestsHandler(),
}

__all__ = [
    'StepHandler',
    'HANDLERS',
    'CommentHandler',
    'SetVariableHandler',
    'IfHandler',
    'ElseIfHandler',
    'ElseHandler',
    'EndIfHandler',
    'ExitScriptHandler',
    'SetErrorCaptureHandler',
    'NewWindowHandler',
    'CloseWindowHandler',
    'EnterPreviewModeHandler',
    'PrintHandler',
    'PerformScriptHandler',
    'GoToLayoutHandler',
    'GoToRecordRequestPageHandler',
    'GoToRelatedRecordHandler',
    'SetFieldHandler',
    'PerformFindHandler',
    'ShowCustomDialogHandler',
    'OpenURLHandler',
    'SendMailHandler',
    'SetFieldByNameHandler',
    'InstallOnTimerScriptHandler',
    'CommitRecordsRequestsHandler',
]
