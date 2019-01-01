import functools
import re
import threading
import time


class ClipboardThread(threading.Thread):
    SLEEP_INTERVAL = 0.1

    def __init__(self, clipboard, filters=[]):
        self.__clipboard = clipboard
        self.__filters = filters

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

    def remove_tracking(self, text):
        return functools.reduce(lambda t, f: re.sub(f, r'\1', t), self.__filters, text)
