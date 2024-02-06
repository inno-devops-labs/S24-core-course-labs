# Time API

## Description

Simple FastApi-based web API that can give you current time in Moscow Standard Time timezone.

## Local setup

### Setup

Prepare the environment:

1. Create venv
2. Install the requirements: `pip install -r requirements.txt`

### Launch

Then you can actually launch the app:

```sh
uvicorn main:app --reload
```

### Interact

Now you can interact with the app. To see the current time in Moscow, visit <http://localhost:8000/time/msk>

## Interactive documentation

To view auto-generated Swagger docs, visit <http://localhost:8000/docs>
