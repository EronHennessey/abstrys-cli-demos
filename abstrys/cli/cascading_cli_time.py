# 
# "Cascading CLI" pattern "time" CLI
#
# This CLI provides a "time" command for the main CLI.

import time
from abstrys.cli.common import CliCommand

class TimeCommand(CliCommand):
    """
    A CLI command that returns the current time.
    """

    def set_up_parser(self, parser):
        """
        Set up the time command arguments.
        """
        parser.add_argument("--timezone", "-tz",
           nargs=1,
           help="return the current time in the given time zone")


    def run(self, args):
        """
        Prints the time.
        """
        vargs = vars(args)

        if vargs['timezone'] != None:
            import os
            os.environ['TZ'] = vargs['timezone'][0]
            time.tzset()

        print("The current time is: " + str(time.ctime()))

