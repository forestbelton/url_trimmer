from sys import stderr
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
        except TypeError as ex:
            if len(ex.args) == 0 or ex.args[0] not in ALLOWED_ERRORS:
                print(f'Failed to retrieve clipboard data: {ex}', file=stderr, flush=True)

        return text

    def set(self, text: str) -> str:
        OpenClipboard()
        EmptyClipboard()
        SetClipboardText(text)
        CloseClipboard()
