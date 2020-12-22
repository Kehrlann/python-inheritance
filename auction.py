from utils import Cli


class BlindAuction():

    def __init__(self, cli=None):
        self.cli = cli if cli else Cli()

    def play(self):
        self.cli.display('Started auction of type: Blind')
        opening = int(self.cli.prompt('Please enter the opening bid:'))
        self.cli.display(f"Opening bid is: {opening}")
