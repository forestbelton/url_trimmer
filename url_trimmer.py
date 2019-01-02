from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

from url_trimmer.clipboard_thread import ClipboardThread
from url_trimmer.clipboard.windows_text_clipboard import WindowsTextClipboard

if __name__ == '__main__':
    # Set up the clipboard thread
    filters = [
        r'(https?://open.spotify.com/track/.+?)(\?[^\s]+)',
        r'(https?://www.amazon.com/.*?/dp/.*?/)(ref=[^\s]+)?'
    ]

    clipboard = WindowsTextClipboard()
    thread = ClipboardThread(clipboard, filters)
    thread.start()

    # Start the system tray icon
    image = Image.open('icon.png')
    icon = Icon('URL Trimmer', icon=image, menu=Menu(
        MenuItem('Settings', lambda icon, item: None),
        MenuItem('Exit', lambda icon, item: icon.stop())
    ))

    icon.run()
