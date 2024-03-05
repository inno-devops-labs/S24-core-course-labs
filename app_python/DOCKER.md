# Docker Best Practices

In this project, several Docker best practices were used.

## Trusted base image

The image is built from official and trusted image, using precise version.

## Vulnerabilities check

At the time of writing, the base image has the least number of vulnerabilities discovered, and derived image does not more.

## Rootless container

The container executes under a non-root user, restricting privileges.

## `COPY` instead of `ADD`

Where possible, `COPY` was used to be more explicit.

## Layer sanity

Multiple `COPY` and `RUN` instructions were combined to reduce the number of layers.

## Controlled exposed ports

Only necessary ports were exposed for the application.

## Dockerfile linting

The Dockerfile was formatted using [linter](https://hadolint.github.io/hadolint/).
