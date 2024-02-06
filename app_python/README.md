# How to work with this web application:
## To start the web service:
- fill in the environment variables that should be in `~/app_python/.env`
- next, you need to build and run the docker container (`~/app_python/DockerFile`)
  * ### for example, you can build + run docker container using commands:
    * `docker build -t flask-app .`
    * `docker run -d -p {port-name}:{docker-port-name} --name new_container flask-app`

## For testng:
- Go to the `/localhost:{port-name}`