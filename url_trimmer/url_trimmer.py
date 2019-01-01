from functools import reduce
from re import sub
from threading import Thread
from time import sleep

from url_trimmer.clipboard.windows_text_clipboard import WindowsTextClipboard


class ClipboardThread(Thread):
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

            sleep(ClipboardThread.SLEEP_INTERVAL)

    @staticmethod
    def remove_tracking(text):
        return reduce(lambda t, f: sub(f, r'\1', t), ClipboardThread.URL_FILTERS, text)


if __name__ == '__main__':
    clipboard = WindowsTextClipboard()
    ClipboardThread(clipboard).run()
