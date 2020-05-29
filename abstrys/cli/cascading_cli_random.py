# 
# "Cascading CLI" pattern "random" CLI
#
# This CLI provides a "random" command for the main CLI.

import random
from abstrys.cli.common import CliCommand

class RandomCommand(CliCommand):
    """
    A CLI command that prints a random number
    """

    def set_up_parser(self, parser):
        """
        Set up the time command arguments.
        """
        parser.description = "Prints a random number."
        parser.add_argument("--seed", "-s",
           nargs=1, type=int,
           help="Set the random number seed.")


    def run(self, args):
        """
        Prints a random number
        """
        vargs = vars(args)

        if vargs['seed'] != None:
            random.seed(vargs['seed'][0])

        print(str(random.random()))

