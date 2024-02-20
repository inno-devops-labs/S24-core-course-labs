# Lab 3: CI workflow

## Overview

I followed best practices mentioned in official docs while using CI workflows with GitHub Actions `main.yaml`. For each push, I perform the following checks on the source code files. I'll describe how it works in detail.

## OS and Python version

I am using Ubuntu and Python 3.10 version. In addition, I am caching pip to reduce the time taken by subsequent workflow runs.

## Installing dependencies

This step involves installing dependencies/libraries required for running and testing the app.

## Linting

This step involves running linting checks using `flake8` to ensure code quality.

## Testing

This step involves running automated unit tests using `pytest`.

## Docker

This step involves signing in to the Docker Hub account using credentials which were added to the GitHub repository as secrets, building the image, and pushing it to Docker Hub.

## Snyk Integration 

I have a seperate file `snyk.yaml`, in which, CI workflow installs the Python dependencies, installs the Snyk CLI, authenticates Snyk using the provided API token stored as a secret (SNYK_TOKEN), and then runs the Snyk test to check for vulnerabilities in the Python dependencies.
