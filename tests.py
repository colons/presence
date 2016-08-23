from unittest2 import TestCase

from bs4 import BeautifulSoup
import requests


UA = (
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/41.0.2228.0 Safari/537.36'
)

class PresenceTest(TestCase):
    """
    Make sure everything is still up.
    """

    @classmethod
    def add_check(cls, url, expected_title):
        def check(self):
            resp = requests.get(url, headers={'user-agent': UA})

            got_title, = [
                e.text for e in
                BeautifulSoup(resp.text).select('title')
            ]
            self.assertEqual(
                got_title.strip(), expected_title,
                '{url} is bad\n{got!r} != {exp!r})'.format(
                    url=url, got=got_title.strip(), exp=expected_title,
                )
            )

        name = 'test_{url}_{title}'.format(url=url, title=expected_title)
        check.__name__ = name

        setattr(cls, name, check)


for expected_title, urls in [
    ('a neko desu request robot | nkd.su', [
        'http://nkd.su/',
        'https://nkd.su/',
        'http://www.nkd.su/',
    ]),
    ('Barry Watson - Raconteur & Musician', [
        'http://barrywatson.co/',
        'http://www.barrywatson.co/',
    ]),
    ('Home | Music for the Blind', [
        'http://musicfortheblind.co.uk/',
        'http://www.musicfortheblind.co.uk/',
        'http://bldm.us/',
        'http://www.bldm.us/',
    ]),
    ('i am a cool internet person', [
        'http://colons.co/',
        'https://colons.co/',
        'http://www.colons.co/',
        'https://www.colons.co/',
        'http://nivi.org.uk/',
        'http://www.nivi.org.uk/',
        'http://dump.musicfortheblind.co.uk/',
    ]),
    ('irc.biz.ru:6697', [
        'http://ggj14.colons.co/',
    ]),
    ('lp', [
        'http://lp.colons.co/',
    ]),
    ('Music | Sanity Valve', [
        'http://sanityvalve.com/',
        'http://www.sanityvalve.com/',
    ]),
    ('The Music for the Blind Review', [
        'http://opinions.colons.co/',
        'http://opinions.musicfortheblind.co.uk/',
        'http://opinions.bldm.us/',
    ]),
    ('trenchfoot', [
        'http://woof.colons.co/',
    ]),
    ('The Latest Scoops!', [
        'http://hotscoops.co/',
        'http://www.hotscoops.co/',
        'https://hotscoops.co/',
    ]),
    ("vinny's profile", [
        'http://giantasshole.com/',
        'http://www.giantasshole.com/',
    ]),
    ("Very Scary Scenario", [
        'http://vscary.co/',
        'https://vscary.co/',
    ]),
    ("Extraction Chamber", [
        'http://ec.vscary.co/',
        'https://ec.vscary.co/',
    ]),
]:
    for url in urls:
        PresenceTest.add_check(url, expected_title)
