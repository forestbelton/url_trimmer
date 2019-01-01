from .text_clipboard import TextClipboard


class StubClipboard(TextClipboard):
    def __init__(self):
        self.__text = ''

    def get(self) -> str:
        return self.__text

    def set(self, text: str) -> None:
        self.__text = text
