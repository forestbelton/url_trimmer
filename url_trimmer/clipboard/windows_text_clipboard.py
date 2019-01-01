from win32clipboard import OpenClipboard, GetClipboardData, EmptyClipboard, SetClipboardText, \
    CloseClipboard
from .text_clipboard import TextClipboard

class WindowsTextClipboard(TextClipboard):
    def get(self):
        text = ''

        try:
            OpenClipboard()
            text = GetClipboardData()
            CloseClipboard()
        except Exception as err:
            print(f'Failed to retrieve clipboard data: {type(err)} {err}', file=sys.stderr, \
                  flush=True)

        return text

    def set(self, text):
        OpenClipboard()
        EmptyClipboard()
        SetClipboardText(text)
        CloseClipboard()
