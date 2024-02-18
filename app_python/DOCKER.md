## 1. Best practices applied within my Dockerfile

### Minimal Image

To make my Docker image tiny, I've utilized a basic image with minimal size.

### Caching

Caching has been employed by me to expedite the construction process.
I have merely updated the image with the required files and folders.

### User

To execute my program within the container, I haven't utilized the root user.
For security purposes, it is recommended to execute the program as a non-root user.

### Layer Sanity

In my Docker image, I have minimized the amount of layers.
It facilitates comprehension and upkeep of the picture.

### Publishing

My Docker image is now available on a container registry.
It facilitates the sharing and deployment of my application.

### Dockerfile Linting

I linted my Dockerfile using the web tool to make sure it adheres to standard practices.

### Dockerignore

To remove superfluous files and directories from the Docker context, I have used a `.dockerignore} file.
This helps to decrease the size of the Docker image and expedite the build process.