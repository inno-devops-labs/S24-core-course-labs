# Dockerfile Best Practices

- Use multi-stage build to copy in the final image only the necessary build output to reduce its size 
- Use official Docker image with its precise version
- Use the minimum number of layers to reduce the image size and build time
- Use `COPY` instead of `ADD`
- Use EXPOSE to show the container listens on specific network ports at runtime
- Use `.dockeringnore` to have a smaller and restricted build context that will make builds faster
- Use Haskell Dockerfile Linter for quality assurance
- Add clear comments in the Dockerfile to describe instructions