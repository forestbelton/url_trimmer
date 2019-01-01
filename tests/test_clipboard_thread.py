from url_trimmer.url_trimmer import ClipboardThread
from url_trimmer.clipboard.stub_clipboard import StubClipboard

clipboard = StubClipboard()


def test_remove_tracking__matches_url_pattern():
    raw = 'https://open.spotify.com/track/1PLEtjblh2EHJlVVIDB84O?si=TQEmHpn1Vf2kNvdcRT87Ng'
    stripped = 'https://open.spotify.com/track/1PLEtjblh2EHJlVVIDB84O'
    thread = ClipboardThread(clipboard, [r'(https?://open.spotify.com/track/.+?)(\?[^\s]+)'])

    exact = thread.remove_tracking(raw)
    assert exact == stripped

    suffix = thread.remove_tracking(f'A {raw}')
    assert suffix == f'A {stripped}'

    prefix = thread.remove_tracking(f'{raw} B')
    assert prefix == f'{stripped} B'

    middle = thread.remove_tracking(f'A {raw} B')
    assert middle == f'A {stripped} B'


def test_remove_tracking__no_match():
    orig = 'there is no match here'
    thread = ClipboardThread(clipboard)

    assert orig == thread.remove_tracking(orig)
