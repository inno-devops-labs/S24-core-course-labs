# Vite React Moscow Time Web Application
![tests](https://github.com/slry/S24-core-course-labs/actions/workflows/typescript_tests.yml/badge.svg?branch=lab1)
![docker](https://github.com/slry/S24-core-course-labs/actions/workflows/docker_build_typescript.yml/badge.svg?branch=lab2)

## Overview
Simple App that shows current Moscow Time

## Requirements
- Node 16 or higher
- Node Package Manager (npm)

## Installation
- Clone this repository
```bash
git clone https://github.com/slry/S24-core-course-labs.git -b lab1
cd S24-core-course-labs
cd app_typescript
```
- Install dependencies
```bash
npm install
```

## Usage
To run application
```bash
npm run dev
```

Go to http://127.0.0.1:5173

## Usage Docker
- Pull image
```bash
docker pull slry/typescript_moscow_time
```
- Run Container
```bash
docker run -p 8080:8080 slry/typescript_moscow_time
```

Go to http://127.0.0.1:8080

## Unit Tests
Unit tests are written using `React Testing Library (RTL)` and `Jest`

All unit tests are located in `src/tests/unit` directory

On every `push` and `pull_request` gh action runs Jest and ESLint on project

To run unit tests
```bash
npm run test
```


## CI Workflows

- `typescript_tests.yml` 
    - action triggers only on changes that occures in `app_typescript/**`
    - lint -> test -> snyk security check

- `docker_build_typescript.yml`
    - action triggers only on changes that occures in `app_typescript/**` files, Dockerfile and requirements.txt
    - action lints dockerfile, builds image and uploads it to Dockerhub
