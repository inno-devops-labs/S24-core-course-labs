init:
	python3 -m venv venv
	. venv/bin/activate; pip install -r requirements.txt; pre-commit install
	@echo "\n\033[0;32mYour dev environment is ready!\033[0m\n"

run:
	. venv/bin/activate; bash start.sh

docker-run:
	docker run -p 8000:8000 --rm -ti devops-lab-02-python

docker-build:
	docker build . -t devops-lab-02-python

docker-pull:
	docker pull adarika/devops-lab-02-python

docker-pull-run: docker-pull
	docker run -p 8000:8000 --rm -ti adarika/devops-lab-02-python

docker-push:
	docker tag devops-lab-02-python  adarika/devops-lab-02-python
	docker push adarika/devops-lab-02-python

test:
	. venv/bin/activate; PYTHONPATH=. pytest tests -W ignore::DeprecationWarning

format:
	( \
		. venv/bin/activate; \
		isort app; isort tests; \
		black app; black tests; \
	)

lint-check:
	. venv/bin/activate; flake8 app; flake8 tests; pylint app; refurb --enable-all app

typecheck:
	. venv/bin/activate; pyright app