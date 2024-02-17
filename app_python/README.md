# Python Web Application: Moscow Time Display

This is a simple web application built with Python and Flask framework to display the current time in Moscow.

## Features

- Displays the current time in Moscow.
- Automatically updates the time upon page refreshing.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/fatm1nd/devops-core-innopolis-course
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to `http://127.0.0.1:5000/` to view the current time in Moscow.

## Project Structure

```python
app_python/
│
├── app.py # Main application file
├── templates/ # HTML templates
│ └── index.html # Main HTML template
├── static/ # Styles, scripts and etc
│ ├── script.js
│ └── styles.css
├── static/ # Unit tests
│ └── test_app.py
├── .gitignore # Git ignore file
├── .dockerignore # Ignore files during building Docker container
├── Dockerfile # Dockerfile itself :D
└── requirements.txt # Required dependencies
```

## Docker

### Build

(You can skip this section and just pull imafge from Docker Hub - `docker pull fatm1nd/devops-lab-container`)

Build app in root repo directory:

```
docker build -t devops-lab-container ./app_python/
```

and also you can tag your image (for adding to registry):
```
docker tag devops-lab-container fatm1nd/devops-lab-container
```


### Pull

You can also pull image from Docker Hub registry (but you can `run` it and it would pull automatically)

```
docker pull fatm1nd/devops-lab-container
```

### Run

You can run application with specific parameters:

```
docker run -p 5001:5000 devops-lab-container
```

Also you could run built image from Docker Hub:
```
docker run -p 5001:5000 fatm1nd/devops-lab-container
```

After that your applications would be available on https://localhost:5001

## Unit Tests

1. Test if get_moscow_time returns the current time.

2. Test if index route returns the current time.

3. Test if defined text is displayed on web page

4. Test if download speed is enough (very fast)

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).