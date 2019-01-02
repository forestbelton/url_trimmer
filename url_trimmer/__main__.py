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
    thread.stop()
    icon.stop()


def main():
    global thread
    thread = ClipboardThread(WindowsTextClipboard(), DEFAULT_FILTERS)
    thread.start()

    image = Image.open('icon.png')
    icon = Icon('URL Trimmer', icon=image, menu=Menu(
        MenuItem('Settings', lambda icon, item: None),
        MenuItem('Exit', close_app)
    ))

    icon.run()

if __name__ == '__main__':
    main()
