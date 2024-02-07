# Web App That Shows Time In Moscow

## Docs

Can be accessed while running: `/docs`

>> Get `/api/v1/time`
>
> Returns current time in Moscow in the following json format:
>
> `{ "time": "07:41:56.120960" }`

## How to run

1. Install python 3.9+ from [official website](https://www.python.org/)
2. Clone repository
3. Create virtual environment (optional) and activate it:
```shell
python3 -m venv venv
```
```shell
source venv/bin/activate
```
4. Install dependencies:
```shell
pip install -r requirements.txt
```
5. Execute main:
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