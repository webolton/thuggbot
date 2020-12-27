from ..exceptions.exceptions import IllegalArgumentError


class Helpers:

    @staticmethod
    def validate_argument(cli_arg):
        """
        Validates commandline arguments
        """
        if (cli_arg == 'cat') or (cli_arg == 'human'):
            return True

        raise IllegalArgumentError('Must use "cat" or "human" for argument.')
