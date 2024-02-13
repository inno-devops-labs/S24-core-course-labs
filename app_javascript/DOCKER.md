While creating a Docker image for my application, I used the following Docker best practices:

1. I created `.dockerignore` file to exclude unnecessary and sensitive files from the Docker image.
2. I created a non-root user in the Docker image to run the application.
3. I put instructions that are less likely to change at the top of the Dockerfile, and the ones that are more likely to change at the bottom, so that the Docker cache can be used effectively.
4. I used the official trusted Node image and explicitly specified the version of the base image (i.e. didn't use `latest` tag).
5. I used Alpine as the base image to reduce the size of the Docker image.
6. I copied files using the `COPY` instruction instead of `ADD` instruction, since `COPY` is more explicit.
7. I explicitly specified the exposed port in the Dockerfile.
8. I used multi-stage builds to reduce the size of the Docker image.
