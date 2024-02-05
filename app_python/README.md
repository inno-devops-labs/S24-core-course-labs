# Current Moscow Time

A simple web application that shows the current time in Moscow.

```
$ curl localhost:8080
2024-02-05T21:58:51.772798+03:00
```

## Installation

Ensure that you have Python 3 installed. After that, install the required
packages using `pip`, possibly inside a virtual environment.

```bash
pip3 install -r requirements.txt
```

## Running

```bash
python3 src/main.py
```

If everything is okay, you'll see the following output. Now you can make
requests to `localhost:8080` to fetch the current Moscow time.

```
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```
