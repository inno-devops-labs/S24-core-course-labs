# Docker best practices 
For my implementation I followed the following practices:
* minimal image size: I have used `python:3.10.13-alpine3.19` as a base image to minimize the size of my image;
* specified WORKDIR: I specified work dir to avoid default parameters and make `Dockerfile` more readable;
* non-root user: I created a new user inside the image to run my app;
* used copy for specific files: I copied the folder `/src` with the main Python code and `requirements.txt` for future
dependencies installation;
* caching while packages installation: I used `--no-cache-dir` to increase the speed of image building and reduce 
possible image's size;
* post expose: I exposed 8080 port for the future port usage;
* CMD command;
* minimal number of `Dockerfile` lines;
* Docker Hub publishing: published in `sokolofff/app_python` repo;
* Docker linting via `pre-commit`;
* `.dockerignore` file: this files ignores unneeded files and dirs to minimize image size.