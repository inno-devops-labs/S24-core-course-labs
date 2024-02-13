## Best Practices in Dockerfile

Best practices that applied for the Rust application are likely to those
used for the python application - [Docker Best Practices for Python](../app_python/DOCKER.md).

Also I have check some info about **Multi-stage builds**: 

> Multi-stage builds are useful to anyone who has struggled to optimize Dockerfiles while keeping them easy to read and maintain.
> 
> from [Docker docs mannuals](https://docs.docker.com/build/building/multi-stage/)

and then apply idea in `Dockerfile` for `app_rust`.

### Docker image

Access with a link `https://hub.docker.com/repository/docker/adarika/devops-lab-02-rust/general`

Or pull image via `docker pull adarika/devops-lab-02-rust`