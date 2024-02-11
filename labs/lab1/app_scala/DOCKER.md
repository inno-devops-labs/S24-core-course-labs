# Docker

## Best practices used

- Minimal Base Image: The image uses
  `sbtscala/scala-sbt:eclipse-temurin-focal-17.0.10_7_1.9.8_3.3.1`(for running tests and compiling), which is a
  minimal base image suitable for Scala sbt applications, and
  `eclipse-temurin:17.0.10_7-jre-jammy`(for executing app), which is the minimal base for jvm
  applications.
- Non-Root User: Non-root user `appuser` is used by default
  for the container, which reduces the risk associated with running
  processes as root.
- Copy Instructions: The COPY instructions are used instead of ADD, which is
  more explicit and less error-prone.
- Explicit Entrypoint: The image specifies an ENTRYPOINT to define the default
  executable for the container, which is a good practice.
- Multi-stage builds: This image contains multiple stages: the first one for
  building and testing and the second one for executing an application. Such
  setup allows reducing an image size and number of dependencies which means
  smaller attack surface
