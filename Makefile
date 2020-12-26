MODULE := thuggs

run:
	@python3 -m $(MODULE)

test:
	@pytest

lint:
	find . -type f -name "*.py" | xargs pylint
