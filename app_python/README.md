# Python Web Application - Moscow Time

## Overview

This is a simple web application developed in Python using the Flask framework to display the current time in Moscow.

## Installation

1. Clone the repository:

```
git clone https://github.com/hermandyudin/S24-core-course-labs.git
cd app_python
```

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Running the Application

```
python app.py
```

Visit http://127.0.0.1:5000/ in your browser to view the work of the application.

## Docker

### Build

To get and run the Docker image, use the following commands:

```bash
docker pull Dudukk/devops:latest .
docker run -p 5000:5000 Dudukk/devops:latest .