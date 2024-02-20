# Lab1 Python web application for time

[![Python App CI](https://github.com/y4cer/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)](https://github.com/y4cer/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)



## Overview

This app displays current time in Moscow timezone, updating every second.

## Installation

### Prerequisites

- Python 3.x
- pip manager

### Installation steps

- Clone the repository

 ```bash
 git clone git@github.com:y4cer/S24-core-course-labs.git
 ```

- Navigate to the application directory

```bash
cd S24-core-course-labs/app_python
```

- Install requirements

 ```bash
 pip install -r requirements.txt
 ```

## Usage

1. `uvicorn app:app --reload`
2. Open the `http://127.0.0.1:8000/` in browser for current time


## Docker

You can either build the image by yourself by:
- Navigate to the application directory

```bash
cd S24-core-course-labs/app_python
```

- Build the image

```bash
docker build -t <tag_here> .
```

- Run the image

```bash
docker run <tag_here>
```
