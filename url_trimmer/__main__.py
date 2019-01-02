import logging
from pystray import Icon, Menu, MenuItem
from PIL import Image

from .clipboard_thread import ClipboardThread
from .clipboard.windows_text_clipboard import WindowsTextClipboard

thread = None
DEFAULT_FILTERS = [
    r'(https?://open.spotify.com/track/.+?)(\?[^\s]+)',
    r'(https?://www.amazon.com/.*?/dp/.*?/)(ref=[^\s]+)?'
]


def close_app(icon, item):
    logging.info('Waiting for clipboard thread to exit')
    thread.stop()
    thread.join()

    logging.info('Stopping system tray icon')
    icon.stop()


def main():
    logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
    logging.info('URL Trimmer boot!')

    global thread
    thread = ClipboardThread(WindowsTextClipboard(), DEFAULT_FILTERS)

    logging.info('Starting clipboard thread')
    thread.start()

    image = Image.open('icon.png')
    icon = Icon('URL Trimmer', icon=image, menu=Menu(
        MenuItem('Settings', lambda icon, item: None),
        MenuItem('Exit', close_app)
    ))

    logging.info('Starting system tray icon')
    icon.run()

if __name__ == '__main__':
    main()
