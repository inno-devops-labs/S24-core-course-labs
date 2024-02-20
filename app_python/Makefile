build:
	pipenv install

run:
	pipenv run uvicorn app.main:app --reload

start: build run

remove:
	pipenv --rm
	pipenv --clear
