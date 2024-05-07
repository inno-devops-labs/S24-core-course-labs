# syntax=docker/dockerfile:1

FROM python:3.8-slim

# Create new user named user
RUN useradd user -ms /bin/bash

# Create directory for the user
RUN mkdir -p /app && chown -R user:user /app

# switch to the user
USER user

# set the working directory
WORKDIR /

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy after starting installing the requirements
COPY app/* /app/
COPY tests/* /tests/

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
