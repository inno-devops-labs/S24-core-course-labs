# Date and Time in Moscow

## Table of Content

<!--toc:start-->
- [Date and Time in Moscow](#date-and-time-in-moscow)
  - [Table of Content](#table-of-content)
  - [Overview](#overview)
  - [Running](#running)
    - [Using Docker](#using-docker)
    - [Using Docker Compose](#using-docker-compose)
    - [Locally](#locally)
<!--toc:end-->

## Overview

An app that displays Moscow date and time that should be agnostic to the
timezone of the environment it is run on.

Application is written in Python using Flask, see [PYTHON.md](./PYTHON.md) for
more details

## Running

### Using Docker

You may use already built image:

```sh
docker pull skril/moscow-time:python
docker run -p 8080:8080 skril/moscow-time:python
```

Or build it yourself:

```sh
docker build -t moscow-time .
docker run -p 8080:8080 moscow-time
```

Now an app can be accessed at http://localhost:8080

### Using Docker Compose

The simplest way to run the app is to:

```sh
docker compose up
```

### Locally

Requirements:

- `Python 3.11.6`

Install dependencies

```bash
pip install -r requirements.txt
```

And then run application

```bash
python3 main.py
```

It can be accessed on http://localhost:8080/
