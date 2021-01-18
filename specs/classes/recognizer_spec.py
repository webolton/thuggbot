from specs.context import Recognizer, exceptions
from mamba import description, context, it
from expects import expect, equal, raise_error


with description('Recognizer') as self:
    with description('#__init__') as self:
        recognition_type = ''

        with it('when it has the correct argument "cat"'):
            recognition_type = 'cat'
            expect(Recognizer(recognition_type)).not_to(
                raise_error(exceptions.IllegalArgumentError))

        with it('when it has the correct argument "human"'):
            recognition_type = 'human'
            expect(Recognizer(recognition_type)).not_to(
                raise_error(exceptions.IllegalArgumentError))

        with it('when it is given an invalid argument'):
            recognition_type = 'rats'
            expect(lambda: Recognizer(recognition_type)).to(
                raise_error(exceptions.IllegalArgumentError))

    with description('#get_cascade') as self:
        recognition_type = 'human'
        pass
