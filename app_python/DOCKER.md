# Best practices I used to Dockerize an application

## Best practice 1
Run as a non-root user, since it is much safer

## Best practice 2
I firstly copy and install Python dependencies and only then I copy the app itself. 
It allows me to use such feature of Docker as **caching**.

If I change only app files, copying and installing dependencies will 
be loaded from the cache since it is not affected.

## Best practice 3
Copy only necessary files and use `.dockerignore`

## Best practice 4
I used this [Docker linter](https://hadolint.github.io/hadolint/) in order to check my Dockerfile.
