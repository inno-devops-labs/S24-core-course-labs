# Python App

This is a simple web application that displays the current time in Moscow. The application is developed using Python and Flask framework.

- [Python App](#python-app)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation Steps](#installation-steps)
  - [Development](#development)
    - [Notes](#notes)

## Installation

### Requirements

- Python 3.8 or higher
- `pip` package manager

### Installation Steps

- Clone this branch to your local machine

```bash
git clone git@github.com:pptx704/S24-devops-labs -b lab1
```

- Navigate to the `app_python` folder

```bash
cd app_python
```

- Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the required packages

```bash
pip install -r requirements.txt
```

- Run the application

```bash
flask run
```

The application will be available at [localhost:5000](http://localhost:5000/)

![Screenshot](https://i.postimg.cc/XYVk7s95/image.png)

## Development

Contributions are not accepted at the moment as this is just a lab assignment. You can fork the repository for your own use.

### Notes

The application uses several pre-commit hooks. Make sure that your system has `pylint`, `black` and `mypy` installed. Or alternatively, you can commit with the virtual environment activated. To skip the pre-commit hooks, use the `--no-verify` flag with the `git commit` command.
