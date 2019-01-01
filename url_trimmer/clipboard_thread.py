import functools
import re
import threading
import time

from .clipboard.text_clipboard import TextClipboard
from typing import Sequence


class ClipboardThread(threading.Thread):
    SLEEP_INTERVAL = 0.1

    def __init__(self, clipboard: TextClipboard, filters: Sequence[str] = []) -> None:
        threading.Thread.__init__(self)
        self.__clipboard = clipboard
        self.__filters = filters

    def run(self) -> None:
        print('Starting!', flush=True)

        while True:
            text = self.__clipboard.get()

            if len(text) != 0:
                pruned = self.remove_tracking(text)
                if pruned != text:
                    self.__clipboard.set(pruned)
                    print(f'Pruned "{text}" to "{pruned}"', flush=True)

            time.sleep(ClipboardThread.SLEEP_INTERVAL)

    def remove_tracking(self, text: str) -> str:
        return functools.reduce(lambda t, f: re.sub(f, r'\1', t), self.__filters, text)
