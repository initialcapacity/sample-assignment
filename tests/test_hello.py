import unittest

import responses

from sample.hello import message


class TestHello(unittest.TestCase):
    @responses.activate()
    def test_hello(self):
        responses.get("https://messages.example.com", status=200, body="there everyone!")

        self.assertEqual("Hello there everyone!", message("https://messages.example.com"))
