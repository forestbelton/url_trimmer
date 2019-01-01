from sys import stderr
from win32clipboard import OpenClipboard, GetClipboardData, EmptyClipboard, SetClipboardText, \
    CloseClipboard
from .text_clipboard import TextClipboard


class WindowsTextClipboard(TextClipboard):
    def get(self) -> str:
        text = ''

        try:
            OpenClipboard()
            text = GetClipboardData()
            CloseClipboard()
        except Exception as err:
            print(f'Failed to retrieve clipboard data: {type(err)} {err}', file=stderr,
                  flush=True)

        return text

    def set(self, text: str) -> str:
        OpenClipboard()
        EmptyClipboard()
        SetClipboardText(text)
        CloseClipboard()
