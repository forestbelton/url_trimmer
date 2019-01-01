import abc
import re
import sys
import threading
import time
import win32clipboard

from functools import reduce


class ClipboardThread(threading.Thread):
    SLEEP_INTERVAL = 0.1
    URL_FILTERS = [
        r'(https?://open.spotify.com/track/.+?)(\?[^\s]+)',
        r'(https?://www.amazon.com/.*?/dp/.*?/)(ref=[^\s]+)?'
    ]

    def __init__(self, clipboard):
        self.__clipboard = clipboard

    def run(self):
        print('Starting!', flush=True)

        while True:
            text = self.__clipboard.get()

            if len(text) != 0:
                pruned = ClipboardThread.remove_tracking(text)
                if pruned != text:
                    self.__clipboard.set(pruned)
                    print(f'Pruned "{text}" to "{pruned}"', flush=True)

            time.sleep(ClipboardThread.SLEEP_INTERVAL)

    @staticmethod
    def remove_tracking(text):
        return reduce(lambda t, f: re.sub(f, r'\1', t), ClipboardThread.URL_FILTERS, text)


class TextClipboard(abc.ABC):
    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def set(self, text):
        pass


class WindowsTextClipboard(TextClipboard):
    def get(self):
        text = ''

        try:
            win32clipboard.OpenClipboard()
            text = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
        except Exception as err:
            print(f'failed to retrieve clipboard data: {type(err)} {err}', file=sys.stderr)

        return text

    def set(self, text):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(text)
        win32clipboard.CloseClipboard()


if __name__ == '__main__':
    clipboard = WindowsTextClipboard()
    ClipboardThread(clipboard).run()
