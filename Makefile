MODULE := thuggs

run:
	@python -m $(MODULE) $(type)

test:
	@pytest

specs:
	@python run mamba

lint:
	find . -type f -name "*.py" | xargs pylint

reqs:
	@python -m pip freeze > requirements.txt

setup:
	@python -m pip install -r requirements.txt

.PHONY: test lint
