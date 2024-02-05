# Common base for all the stages
FROM python:3.10-alpine3.19 as common-base

# Define working directory for docker
WORKDIR /code

# Create a user and give user rights to work with required directories
RUN adduser -D myuser && chown -R myuser /code

RUN mkdir /install && chown -R myuser /install

# Change docker user
USER myuser

# Add to the path the bin of new user
ENV PATH="$PATH:/home/myuser/.local/bin"


# The building stage
FROM common-base as builder

# Copying the requirements to working directory
COPY ./requirements.txt /code/requirements.txt

# Upgrading pip
RUN pip3 install --upgrade pip

# Installing python requirements
RUN pip3 install --no-cache-dir --prefix=/install --upgrade -r /code/requirements.txt


# The deploy stage where we copy only files required for project operation and define entrypoint
FROM common-base

# Copy all the installations from buiding stage
COPY --from=builder /install /usr/local

# Copy the the app to the working directory
COPY . /code/app_python

# Define entrypoint
ENTRYPOINT ["uvicorn", "app_python.main:app", "--host", "0.0.0.0", "--port", "80"]