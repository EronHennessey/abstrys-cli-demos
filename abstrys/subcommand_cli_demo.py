#!/bin/env python3
# 
# "Cascading CLI" pattern main CLI
#
# This CLI is the "master" CLI which invokes a number of sub-CLIs

import argparse
from abstrys.cli.cascading_cli_quote import QuoteCommand
from abstrys.cli.cascading_cli_random import RandomCommand
from abstrys.cli.cascading_cli_time import TimeCommand

# Some people recommend using textwrap.dedent() or something to format help
# text. I find it simplest to just make it a triple-quoted block of text
# formatted to the left margin.
DESCRIPTION = """
A demo CLI with subcommands.

The following sub-commands are available:

* quote  - print a random quote.
* random - print a random number.
* time   - print the current time.

You *must* pick one. For sub-command help, add the '--help' flag after the
command name."""

def main():
    """
    Parse the command-line arguments using argparse and run the sub-command
    specified on the command-line.
    """

    # By using RawTextHelpFormatter, my DESCRIPTION is printed as I have it
    # formatted, instead of combined into one continuous line of text (the
    # default).
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        description=DESCRIPTION)

    # Add subparsers, and make choosing one of them *required*.
    # Note: Without 'dest' set, add_subparsers() results in a runtime error when
    # required=True.
    subparsers = parser.add_subparsers(required=True, dest="subcommand")

    # Set up each command. The __init__() method sets up both the parser and the
    # function to run when the sub-command is selected. See
    # abstrys/cli/common.py for details.
    QuoteCommand(subparsers.add_parser("quote"))
    RandomCommand(subparsers.add_parser("random"))
    TimeCommand(subparsers.add_parser("time"))

    # Parse the command line args then run the function associated with the
    # sub-command that was passed in.
    args = parser.parse_args()
    args.func(args)

