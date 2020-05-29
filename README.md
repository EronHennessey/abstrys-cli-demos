# Abstrys CLI Demos

This repository contains a number of CLI demos that represent Python + argparse patterns for
creating various types of CLIs.

I strive toward easy-to-reuse, extensible design, and these demo CLIs are based upon this philosophy.

All the code is in the `abstrys` directory, here's a guide:

## subcommand_cli_demo.py

This is a demo of a 'master' cli with subcommands (similar to `git`), each with their own set of
arguments.

Each subcommand is represented by a "CliCommand" class (in `src/abstrys/cli_common.py`) derivative
that implements two methods:

* `set_up_parser(self, parser)`
* `run(self, args)`

This allows encapsulation of each sub-command within its own source file, and makes adding a
sub-command to the main CLI a one-line affair:

    QuoteCommand(subparsers.add_parser("quote"))

