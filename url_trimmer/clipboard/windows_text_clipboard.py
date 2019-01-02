import logging
from win32clipboard import OpenClipboard, GetClipboardData, EmptyClipboard, SetClipboardText, \
    CloseClipboard
from .text_clipboard import TextClipboard


ALLOWED_ERRORS = [
    'Specified clipboard format is not available'
]


class WindowsTextClipboard(TextClipboard):
    def get(self) -> str:
        text = ''

        try:
            OpenClipboard()
            text = GetClipboardData()
            CloseClipboard()
        except Exception as ex:
            if len(ex.args) == 0 or ex.args[0] not in ALLOWED_ERRORS:
                logging.error(f'Failed to retrieve clipboard data: {ex}')

        return text

    def set(self, text: str) -> None:
        try:
            OpenClipboard()
            EmptyClipboard()
            SetClipboardText(text)
            CloseClipboard()
        except Exception as ex:
            if len(ex.args) == 0 or ex.args[0] not in ALLOWED_ERRORS:
                logging.error(f'Failed to set clipboard text: {ex}')
