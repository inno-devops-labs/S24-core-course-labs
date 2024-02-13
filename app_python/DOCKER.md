# Lab 2

## Best practices

* ### Rootless containers

In Dockerfile, I created new user and use this user to do all the work inside the container.

* ### No binding to a specific UID

I avoided binding to a specific UID because it may break the service.

* ### Making executables owned by root and not writable

I built everything with root and then switched to the `myuser` before entering the entrypoint.

* ### Multistage builds

I applied the multistage building to reduce the size of the image and to reduce attack surface.

* ### Using trusted base images

I used trusted base image python:3.10-alpine3.19. This one was mentioned in the problem statement.

* ### Exposed ports

Avoided exposing ports. I left it for running stage, because we do not want our container to have extra exposed ports.
This ports can play as an entrypoint for attackers.

* ### ADD, COPY

Avoided using ADD command. Used only COPY command.

* ### Using dockerignore

I used `.dockerignore` to exclude all the files that I don't want to see in my image.

* ### Layer sanity

Structure of my `Dockerfile` is quite good. The instructions keep the correct order so the caching is done in correct
way.

* ### Linting

I used Docker linter [Haskell Dockerfile Linter (hadolint)](https://hadolint.github.io/hadolint/) recommended
by authors.
