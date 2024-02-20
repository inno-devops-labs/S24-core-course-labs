build:
	pipenv install

run:
	pipenv run uvicorn app.main:app --host 0.0.0.0 --port 8000
  
start: build run

remove:
	pipenv --rm
	pipenv --clear
