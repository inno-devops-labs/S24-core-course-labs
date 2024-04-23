# Time app

A simple app that displays a time.

Consists of two parts

1. Python API server that uses FastAPI
2. Frontend client

Server has three endpoints

1. `/` for serving static files under [./static](./static) folder
2. `/api/time?tz={tz}` route that accepts timezone and returns the time in this
   timezone in a format of `%Y-%m-%d %H:%M:%S`
3. `/visits` for displaying total number of visits (api accesses)

Client fetches the time on interval each second.

## Docker

### Build

```shell
docker compose up --build
```

### Pull

```shell
docker pull metafates/app_python
```

### Run

Once you have pulled an image you have to obtain its ID. You can do it like
this:

```shell
docker image ls
```

```
REPOSITORY             TAG          IMAGE ID       CREATED        SIZE
metafates/app_python   latest       35217bf3132c   25 hours ago   170MB
```

In this example ID is `35217bf3132c`

Now, you can run it like this:

```shell
docker run -p "8000:8000" 35217bf3132c
```

### Unit tests

To run the unit tests execute the following command in the project root
([from here](../))

```
python3 -m unittest discover -s app_python/tests -p test.py
```

### Workflow

The CI workflow consists of the following steps:

- Install project dependencies
- Run code linting using Flake8
- Run automated tests to ensure code quality
