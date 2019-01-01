from abc import ABC, abstractmethod


class TextClipboard(ABC):
    @abstractmethod
    def get(self) -> str:
        pass

    @abstractmethod
    def set(self, text: str) -> None:
        pass
