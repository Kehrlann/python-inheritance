import unittest

from auction import BlindAuction
from testing_utils import make_auction


class TestAuction():

    def __init__(self, cli=None):
        self.cli = cli

    def play(self):
        val = self.cli.prompt("give me your name")
        self.cli.display(val)


class TestEcho(unittest.TestCase):

    def test_echo(self):
        cli = make_auction(TestAuction)
        self.assertEqual(['give me your name'], cli.get_displayed())
        cli.type("hello")
        self.assertEqual(['hello'], cli.get_displayed())
        self.assertEqual([], cli.get_displayed())


class TestBlind(unittest.TestCase):
    def test_setup(self):
        cli = make_auction(BlindAuction)
        self.assertEqual(
            [
                'Started auction of type: Blind',
                'Please enter the opening bid:'
            ],
            cli.get_displayed()
        )
        cli.type('30')
        self.assertEqual(
            [
                'Opening bid is: 30'
            ],
            cli.get_displayed()
        )


if __name__ == "__main__":
    unittest.main()
