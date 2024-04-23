# Python time app
![CI pipeline](https://github.com/Vikono/S24-DevOps/actions/workflows/main.yaml/badge.svg)

The application is showing the current Moscow time that updates upon page reload.

## How to run
1. Install all requirements from requirements.txt using the following command (either inside venv or in global env):
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app using the following command (assume that the current directory is app_python)
   ```bash
   python api/main.py
   ```

## Features
1. To access the main feature use `localhost:5001/`
2. To access number of visits of index page (`/`) - `localhost:5001/visits`
3. To access metrics - `localhost:5001/metrics`

## Testing
Unit and manual testing are used to ensure corectness of the application. 

Manual testing scenario was to refresh the page and check time is changed.

### Unit tests

The unit testing part contains test for checking the correctness of the function that provides formatted time information. 

Time function is mocked with mocked time in different timezones - MSK and NY.

To run unit tests use the following command:
```bash
pytest
```

## Docker

1. **How to build**
You need to be in `app_python` folder to be able to use the following command:
```bash
docker build -t app .
```
This command links image with the tag `app`, that can be used to call it easier further.

2. **How to run**
If you want to run container using `app` image builded locally:
```bash
docker run -d -p 5001:5001 app
```

If you want to pull image from the DockerHub do the following:
- Pull the image using this command:
   ```bash 
   docker pull vikono/devops:latest
   ```
- Then run it:
   ```bash
   docker run -d -p 5001:5001 vikono/devops:latest
   ```
