![example workflow](https://github.com/github/docs/actions/workflows/main.yml/badge.svg)

# Moscow Time ⏳

## Overview
 There is  a web apllication for the DevOps course S24 in the Innopolis University.
 
## Deploy

All this instruction are suitable for MacOS.

1. Clone the repository using https

```
git clone https://github.com/Bavpnet/S24-core-course-labs
cd app_python
```

2. Run requirments file

```
python3 install -r requirements.txt
```
3. Run application on the local host 

```
python3 main.py
```
## Deploy with Docker

1. Clone the git repo

```
git clone https://github.com/Bavpnet/S24-core-course-labs
cd app_python
```

2. Pull Docker image from the Docker Hub

```
docker pull bavpnet/app_python
```

3. Run Docker image

```
docker run bavpnet/app_python
```
## Testing

You can test the application using the following command

```
python3 testing.py
```

## Unit testing

You can test it, by the following command

```
pytest testing.py
```

## CI workflow

There is a pipeline on push trigger. Firstly, ut checks the build with requirments and tests. Next, it checks linting using flake8, after that there is a pipeline for snyk and Docker. Also, I used a github secrets for keys and passwords.