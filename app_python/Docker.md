# Docker Best Practices

## Specific Copy Commands
The `COPY` command is used to copy the `requirements.txt` file into the container before installing the dependencies. This ensures that the dependencies are installed based on the specifications defined in the `requirements.txt` file.

## Non-Root User
To enhance security, a non-root user (`myuser`) is created and used to run the application. This practice helps to mitigate potential security risks associated with running applications as the root user within the container.

## Precise Base Image
The Dockerfile uses a precise version of the Python alpine image (`python:3-alpine3.15`). Specifying a particular version of the base image helps to ensure consistency across deployments and reduces the likelihood of unexpected changes in behavior due to updates in the base image.

## Exposing Ports
The application's port is explicitly exposed using the `EXPOSE` directive. This informs Docker that the container listens on the specified network port at runtime.

## Starting the Application
The `CMD` directive is used to start the Flask application. By specifying the command in this manner, the application will start automatically when the container is run.

