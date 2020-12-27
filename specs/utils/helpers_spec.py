from specs.context import helpers, exceptions
from mamba import description, context, it
from expects import expect, equal, raise_error


with description('Helpers') as self:
    with description('#validate_argument') as self:
        cli_arg = ''
        
        with it('when it has the correct argument "cat"'):
            cli_arg = 'cat'
            expect(helpers.Helpers.validate_argument(cli_arg)).to(equal(True))

        with it('when it has the correct argument "human"'):
            cli_arg = 'human'
            expect(helpers.Helpers.validate_argument(cli_arg)).to(equal(True))

        with it('when it is given an invalid argument'):
            cli_arg = 'rats'
            expect(lambda: helpers.Helpers.validate_argument(cli_arg)).to(raise_error(exceptions.IllegalArgumentError))
