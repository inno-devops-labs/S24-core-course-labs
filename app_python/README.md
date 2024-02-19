# Local
## Prerequizites
- A `python ^3.10` installed
- `pip install -r requirements.dev.txt`
- `pip install -r requirements.txt`

## Run
- Run `python app.py`
- Navigate to `http://localhost:8080/` in your browser

## Unit Tests
- Run `python -m pytest tests/`
- Verify results

# Docker

## Obtain the image
### Build
Execute the following command in the `app_python` directory:

```bash
docker build -t <name:tagname> .
```

### Pull
If you prefer to pull the pre-built image from Docker Hub, you can use the following command:

```bash
docker pull nabuki/devops-lab:latest
```

## Run
Once the Docker image is built or pulled, you can run the container using the following command:

```bash
docker run -p <some host port: p>:8080 nabuki/devops-lab2:v1
```

- Navigate to `http://localhost:<p>/` in your browser