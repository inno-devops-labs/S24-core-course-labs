# Docker

## Best practices

- The container does not run under `root`, but it uses specially created group and user
- Official Eclipse Temurin (OpenJDK) and Gradle images were used
- The base image version was clearly stated: `eclipse-temurin:17-jdk-alpine` and `gradle:8.6-jdk17-alpine`
- Only `8000` (required for app) port is exposed
- The image is built in 2 stages
- Only files that are required for build are copied
- `Dockerfile` was checked using `hadolint`
