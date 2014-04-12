import requests
from unittest2 import TestCase


class PresenceTest(TestCase):
    """
    Make sure everything is still up.
    """


for url in [
    'http://colons.co/',
    'https://colons.co/',
    'http://nkd.su/',
    'https://nkd.su/',
    'http://musicfortheblind.co.uk/',
    'http://hotscoops.co/',
    'http://sanityvalve.com/',
    'http://bldm.us/',
    'http://giantasshole.com/',
    'http://nivi.org.uk/',
]:
    def check(self):
        requests.get(url)

    name = 'test_{url}'.format(**locals())
    check.__name__ = name

    setattr(PresenceTest, name, check)


check = None  # fukken python scopes
