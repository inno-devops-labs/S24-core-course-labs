### Docker image

Access with a link `https://hub.docker.com/repository/docker/adarika/devops-lab-02-python/general`

Or pull image via `docker pull adarika/devops-lab-02-python`

## Practices used in the Dockerfile

1. I have created *rootless container* to make it harder for intruder to "escape" from container to the host system -> I have created a new user and change active user to a new one
   
2. With change of active user I can also protect source files to not be changed by some intruder (banned write access to all users except for owner)
   
3. To reduce the area of possible attacks I have tried to throw out of container all that don't needed, so I have used `python:3.11-slim` image as a base one (where `3.11` is a python version), this is also make my container very small. Yes, `alpine` images are smaller, but there is point about my choice: `alpine`-based image is so far from my python dev setup, so `slim` is more stable for me + testing.
   
   I understand mostly "pros" about `alpine`-based images (security, lightweight, etc), but I prefer `slim` (using `debian:bookworm-slim`) for python.
   
4. Moreover, I have used a trusted image which is widely used by different users + stable Python version.

5. Also, I have only one open port which is mapped to only internal port.

6. I didn't put any secrets inside container as they can be revealed then. Even if I would share some database/MQ/etc credentials, I would use a special tools provided from Docker.

7. I have tried to remove some layers by merging same commands and compound them into one layer

8. No . and ./ targets in `COPY` layers, this is important to not put something wrong inside container. Only specific files.

9. Layer ordering also important because of caching system, so firstly I have added layers with setup-like purpose and dependencies that will be changed rarely, secondly is the entrypoint file and only then I have copied my source code.

10. Docker linter was used for checking Dockerfile (https://hadolint.github.io/hadolint/) + IDE extension (VSCode Docker by Microsoft)
