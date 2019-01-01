import pytest
from url_trimmer.url_trimmer import ClipboardThread


@pytest.mark.parametrize('before,stripped', [
    ('https://open.spotify.com/track/1PLEtjblh2EHJlVVIDB84O?si=TQEmHpn1Vf2kNvdcRT87Ng', 'https://open.spotify.com/track/1PLEtjblh2EHJlVVIDB84O'),  # noqa: E501
    ('https://www.amazon.com/Set-Theory-Cambridge-Mathematical-Textbooks/dp/1107120322/ref=sr_1_2?ie=UTF8&qid=1544134808&sr=8-2&keywords=set+theory', 'https://www.amazon.com/Set-Theory-Cambridge-Mathematical-Textbooks/dp/1107120322/')  # noqa: E501
])
def test_remove_tracking__matches_url_pattern(before, stripped):
    exact = ClipboardThread.remove_tracking(before)
    assert exact == stripped

    suffix = ClipboardThread.remove_tracking(f'A {before}')
    assert suffix == f'A {stripped}'

    prefix = ClipboardThread.remove_tracking(f'{before} B')
    assert prefix == f'{stripped} B'

    middle = ClipboardThread.remove_tracking(f'A {before} B')
    assert middle == f'A {stripped} B'


def test_remove_tracking__no_match():
    orig = 'there is no match here'
    assert orig == ClipboardThread.remove_tracking(orig)
