# 
# "Cascading CLI" pattern "quote" CLI
#
# This CLI provides a "quote" command for the main CLI.

import random
from abstrys.cli.common import CliCommand

QUOTES = [
    "Hello is not the same as goodbye.",
    "Turtles are smaller than elephants. Well, *usually*.",
    "What is that... thing?",
    "I'm hungry. Catfish!!"
]

ERROR_OUT_OF_QUOTES = """
Error: I don't know that many quotes!

Hint: Try picking a number between 0-%s."""

class QuoteCommand(CliCommand):
    """
    A CLI command that prints a random quote. 
    """

    def set_up_parser(self, parser):
        """
        Set up the time command arguments.
        """
        parser.description = "Prints a random quote."
        parser.add_argument("--quotenum", "-n",
           nargs=1, type=int,
           help="Print a particular (not random) quote.")

    def run(self, args):
        """
        Prints a random quote.
        """
        vargs = vars(args)

        quotearg = vargs.get('quotenum', None)
        quote = ""

        if vargs['quotenum'] != None:
            # we allow the user to enter quote numbers between 1-len(QUOTES),
            # but because arrays are zero-based...
            quotenum = vargs['quotenum'][0]-1
            if quotenum < len(quotes):
                quote = quotes[quotenum]
            else:
                # the quote number was out of range.
                print(ERROR_OUT_OF_QUOTES % len(quotes))
                return
        else:
            quote = random.choice(quotes)

        print(quote)

