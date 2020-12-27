MODULE := thuggs

run:
	@python -m $(MODULE) $(type)

test:
	@pytest

specs:
	mamba

lint:
	pycodestyle

reqs:
	@python -m pip freeze > requirements.txt

setup:
	@python -m pip install -r requirements.txt

.PHONY: test lint specs
