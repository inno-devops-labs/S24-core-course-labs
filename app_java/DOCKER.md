# Docker best practices

I have used the same best practices as in `python_app`. Unfortunately, Layer
Sanity practice is useless in this example, because the wholw job of docker
build is to just copy and execute compiled JAR with dependencies.

TLDR: I completely understand the importance of layer sanity, however it's
useless due to oversimplified Dockerfile

## 1. Application JAR file is passed as an ARG

According to [Spring Docs](https://spring.io/guides/topicals/spring-boot-docker)
it's better to simply segregate responsibilities:

- Maven builds the project
- Docker just copies a resulting JAR file
