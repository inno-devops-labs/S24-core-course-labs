# Dockerfile Best Practices

- Rootless container for better security by limiting the container's access to the host system
- Use official Docker image with its precise version and language
- Use the minimum number of layers to reduce the image size and build time
- Put instructions that are least likely to change, and easier to cache, at the top to speed ub the build process
- Use `COPY` instead of `ADD` because it is more predictable and less error-prone
- Use `.dockeringnore` to have a smaller and restricted build context that will make builds faster
- Use Haskell Dockerfile Linter for quality assurance
- Add clear comments in the Dockerfile to describe instructions