from url_trimmer.clipboard_thread import ClipboardThread
from url_trimmer.clipboard.windows_text_clipboard import WindowsTextClipboard

filters = [
    r'(https?://open.spotify.com/track/.+?)(\?[^\s]+)',
    r'(https?://www.amazon.com/.*?/dp/.*?/)(ref=[^\s]+)?'
]

clipboard = WindowsTextClipboard()
thread = ClipboardThread(clipboard, filters)

thread.start()
thread.join()
