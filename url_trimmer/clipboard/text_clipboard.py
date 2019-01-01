from abc import ABC, abstractmethod

class TextClipboard(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def set(self, text):
        pass
