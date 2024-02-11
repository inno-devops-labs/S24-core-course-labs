# Docker Description

## Dockerfile

The Dockerfile is based on the official `oven/bun:1` image. The application is installed in the `/app/app_bun` directory.

## .dockerignore

`.dockerignore` file was not used in this project since only specific files were copied to the container rather than the whole directory.

## Best practices followed

- Specific sha256 was used along with precise tag to keep the build stable.
- Security practices were followed to reduce the attack surface
- Image size was kept as small as possible
- Added metadata to the image and linter was used to ensure the Dockerfile is written properly

### Security Practices

- The application is run as a non-root user
- The active user (`newuser`) had limited permissions (only the `/app/app_bun` and it's home directory was writable)
- Official `oven/bun:1` image was used as the base image
- Multistaged builds was used. Different stages for installing modules and building.
- While publishing the image, `latest` tag was specified to avoid accidental use of outdated images
- No credentials were hardcoded in the Dockerfile
- No ports were exposed in the Dockerfile

### Image Size

- Multiple `RUN` commands were combined to reduce the number of layers
- Multistaged build was used to have smaller final image size

### Other Best Practices

- `LABEL` was used to add metadata to the image
- `hadolint` was used to ensure the Dockerfile is written properly
- Less used commands were used earlier in the Dockerfile to take advantage of Docker's layer caching.