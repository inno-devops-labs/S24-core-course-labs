# Moscow Time Web Application

This is a simple web application that shows the current time in Moscow.

## Getting started locally

### Prerequisites

- Python 3.9+

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

The running app will be available at http://localhost:8000

## Getting started with Docker

### Prerequisites

- Docker

### Usage

Build the image:

```bash
docker build -t majorro/devops-engineering-course:python .
```

or pull it from Docker Hub:

```bash
docker pull majorro/devops-engineering-course:python
```

Run the container:

```bash
docker run -p 8000:8000 majorro/devops-engineering-course:python
```

The running app will be available at http://localhost:8000

## Contact

- [Telegram](https://t.me/majorro228)
