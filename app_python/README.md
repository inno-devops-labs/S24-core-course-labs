# Web App That Shows Time In Moscow

## Docs

Can be accessed while running: `/docs`

> > Get `/api/v1/time`
>
> Returns current time in Moscow in the following json format:
>
> `{ "time": "07:41:56.120960" }`

## How to run

- Install python 3.9+ from [official website](https://www.python.org/)
- Clone repository
- Create virtual environment (optional) and activate it:

```shell
python3 -m venv venv
```

```shell
source venv/bin/activate
```

- Install dependencies:

```shell
pip install -r requirements.txt
```

- Execute main:

```shell
python3 main.py
```

or

```shell
py main.py
```

## Testing

While app is running, tests could be executed.

Run tests (You should be in the virtual environment)

```shell
pytest .
```

---

## Docker

You can execute program in docker container

### Build

Make sure that you docker daemon is running now.

```shell
docker build . -f Dockerfile -t <name_of_container>
```

### Pull from dockerhub

```shell
docker pull ilnurha/lab2:latest
```

### Run

```shell
docker run -p 5000:5000 <name_of_container>
```

If you pulled from dockerhub name of container is "ilnurha/lab2:latest"
