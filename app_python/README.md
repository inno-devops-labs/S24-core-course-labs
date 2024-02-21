## Time showing app

This is the web application that shows current Moscow time.

### Run application locally

1. Install requirements from "requirements.txt", you can do it using command:

```bash
pip install -r requirements.txt
```

2. Apply command to run the application:

```
python -m app
```

Finally, the app is running on http://127.0.0.1:5000

### Test application locally

Use following command to run all tests:

```
pytest test
```

### Docker

#### Building

To build docker image of the app you should do following steps:

1. Clone repository
2. Navigate "app_python" directory of the cloned repository
3. Run the following command

```bash 
docker build -t belowzero1/app_python:v1 .  
```

You can write preferable name instead of `belowzero1/app_python:v1` in the command. also you can add option `--no-cache`
into the command to re-build the app if there is some changes.

### Pulling

Also, there is an option to pull docker image from the Docker Hub. To do it use the following command:

```bash 
docker pull belowzero1/app_python:v1   
```

### Run Docker Container

When you have docker image

```bash
docker run -d -p 5000:5000 belowzero1/app_python:v1   
```

This command will run the container in detached mode (`-d`) and map port 5000 on the host to port 5000 in the container.

Now you can access the application on `http://localhost:5000` in browser.

### Unit Tests
I have several tests:
- Check that application give response without errors
- Check if the application response once and one more time after that,
        then the second responses will differ from the first
- Check if the application response once and one more time after that,
        then the second responses will be more recent time than the first