## Dockerfile best practices and security best practices:
I've implemented such best practises as:
* Use official base image.
* Minimize number of layers. Instructions RUN, COPY, and ADD create layers which can increase build time and size.
* Use COPY instruction instead of ADD. COPY only supports the basic copying of local files into the container, while ADD has some features (like local-only tar extraction and remote URL support) that are not immediately obvious.
* Use .dockerignore as this reduces image size.
* Add comments in dockerfile to describe instructions.
* Run as non-root user to enhance security.
* Use multi-stage build to drastically reduce the size of the final image. For this lab i've implemented multi-stage build only for go application 

## Dockerfile linter 
I've used hadolint to ensure quality of dockerfile.
Command to start linter: 
```
docker run --rm -i hadolint/hadolint < Dockerfile
```