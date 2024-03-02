# Docker best practices

## 1. Usage of a specific trusted lightweight base image

The most common one is Alpine base image with a concrete tag number, in my case
it's `python:3.11-alpine3.18`

## 2. Copying of specific files only

This reduces the attack surface as well

## 3. Rootless UID-independent container

Let us reduce the attack surface according to docker security best practices
link. Moreover I have **disabled the shell** for the user and `chown`'ed all the
files in workdir to this user.

## 4. Dockerignore and linting

I have added `dockerfilelint` pre-commit hook and `dockerignore` file

## 5. Misc. Prefer COPY over ADD, and use explicit EXPOSE

I used these practices as well
