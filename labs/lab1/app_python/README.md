# Date and Time in Moscow

## Table of Content

<!--toc:start-->
- [Date and Time in Moscow](#date-and-time-in-moscow)
  - [Table of Content](#table-of-content)
  - [Overview](#overview)
  - [Running Locally](#running-locally)
<!--toc:end-->

## Overview

An app that displays Moscow date and time that should be agnostic to the
timezone of the environment it is run on.

Application is written in Python using Flask, see [PYTHON.md](./PYTHON.md) for
more details

## Running Locally

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

It can be accessed on http://localhost:5000/
