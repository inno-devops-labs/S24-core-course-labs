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
docker pull nabuki/moscowtime-web:latest
```

## Run
Once the Docker image is built or pulled, you can run the container using the following command:

```bash
docker run -p <some host port: p>:8080 nabuki/moscowtime-web:latest
```

- Navigate to `http://localhost:<p>/` in your browser

# CI/CD with GitHub Actions

## Workflows

### Check codebase
![Check Codebase](https://github.com/Senopiece/S24-core-course-labs/actions/workflows/checks.yml/badge.svg)
- **File**: `checks.yml`
- **Triggers**: Runs on any push.
- **Secrets**:
  - `SNYK_TOKEN` - token for snyk
- **Steps**:
  - Setup Python environment.
  - Install dependencies from `requirements.txt` and `requirements.dev.txt`.
  - Lint codebase with flake8.
  - Run unit tests with pytest.
  - Run snyk.

### Deployment
![Deployment](https://github.com/Senopiece/S24-core-course-labs/actions/workflows/deploy.yml/badge.svg)
- **File**: `deploy.yml`
- **Secrets**:
  - `DOCKER_IMG_NAME` - the image name to be deployed as
  - `DOCKER_USERNAME` - the user to use to deploy
  - `DOCKER_PASSWORD`- user's password
- **Triggers**: Runs when a new release is created.
- **Steps**:
  - Setup Python environment.
  - Install dependencies.
  - Build Docker image with the tag matching the release name and `latest`.
  - Push the Docker image to Docker Hub.

These workflows ensure code quality and facilitate automated deployment, streamlining the development process.
