MODULE := thuggs

run:
	@python -m $(MODULE)

test:
	@pytest

lint:
	find . -type f -name "*.py" | xargs pylint
