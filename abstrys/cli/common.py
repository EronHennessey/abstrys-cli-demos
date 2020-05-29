# Common CLI classes and methods

from argparse import ArgumentParser

class CliCommand:
    """
    A CLI subcommand base class. CLI subcommands can be derived from this class
    simply by overriding the set_up_parser() and run() methods to provide their
    own arguments and behavior.
    """

    def __init__(self, parser):
        """
        Initialize the CLI. Base classes typically do *not* override this, but
        just declare set_up_parser() and run().

        parser - An instance of argparse.ArgumentParser
        """
        self.set_up_parser(parser)
        parser.set_defaults(func=self.run)


    def set_up_parser(self, parser):
        """
        Adds arguments to the supplied ArgumentParser. This is where a CLI
        would add further sub-commands, flags, etc.

        The default implementation, however, does *nothing*.
        """
        pass


    def run(self, args):
        """
        This method is called when the command is invoked. It provides the
        actual logic of the sub-command. Any additional arguments are provided
        by the 'args' parameter.

        The default only prints the args that were passed in.
        """
        print(str(vars(args)))

