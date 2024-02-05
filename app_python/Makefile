init:
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt; pre-commit install
	@echo "\n\033[0;32mYour dev environment is ready!\033[0m\n"

run:
	. venv/bin/activate; bash start.sh

test:
	. venv/bin/activate; PYTHONPATH=. pytest tests -W ignore::DeprecationWarning

format:
	( \
		. venv/bin/activate; \
		flake8 app; \
		pylint app; \
		isort app; \
		refurb app; \
	)

typecheck:
	. venv/bin/activate; pyright app