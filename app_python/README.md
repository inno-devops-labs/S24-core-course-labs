<div align="center">
  <h3 align="center">FastAPI Moscow time application</h3>
</div>
<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This the Python web application that displays the current time in Moscow. This web application is based on FastAPI
and ntplib for correct time ensurance.

Use the `PYTHON.md` to know about Framework choice, testing and best practices.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![FastAPI][FastAPI]][FastAPI-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Here you can find instruction to set up project on your environment.
To get a local copy up and running follow these simple example steps.

### Prerequisites

For local installation you should ensure that you have installed the python 3.10+ on your system.
You can find how to install python here [Python](python.org)

### Installation

First, you should clone the project

```bash
git clone https://github.com/zaqbez39me/S24-DevOps-Labs
```

Second, you should install the virtualenv for you project and activate it.

```bash
python -m venv venv
source venv/bin/activate
```

Third, install the requirements for the project using following command:

```bash
pip install -r ./app_python/requirements.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

### Manual run of the application

Use following command to run the application

```bash
uvicorn app_python.main:app
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi

[FastAPI-url]: https://fastapi.tiangolo.com/

## Docker

### Build

To build the container use the following command

```bash
docker build -t <NAME_OF_AN_IMAGE> app_python/
```

### Pull

To pull an image from dockerhub use

```bash
docker pull zaqbez39me/s24-devops-labs:latest
```

### Run

To run an application use

```bash
docker run -d --name <NAME_OF_CONTAINER> -p <PORT>:80 <NAME_OF_AN_IMAGE>
```

For example,

```bash
docker run -d --name fastapi-moscow-time -p 80:80 zaqbez39me/s24-devops-labs:latest
```

## Unit tests

The tests are located in the `tests` folder.

### Run

To run the unit tests use the following command

```bash
pytest
```