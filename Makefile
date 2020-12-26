MODULE := thuggs

run:
	@python -m $(MODULE) $(type)

test:
	@pytest

lint:
	find . -type f -name "*.py" | xargs pylin

reqs:
	@python -m pip freeze > requirements.txt

setup:
	@python -m pip install -r requirements.txt

.PHONY: test lint

