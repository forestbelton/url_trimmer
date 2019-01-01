from .text_clipboard import TextClipboard

class StubClipboard(TextClipboard):
    def __init__(self):
        self.__text = ''

    def get(self):
        return self.__text

    def set(self, text):
        self.__text = text
