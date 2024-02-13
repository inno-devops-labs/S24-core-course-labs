# Docker best practices used

## Rootless execution
I created a user other than root to run the app. This way if an attacker gets execution privileges, they wouldn't be able to run commands as root.

## Up-to-date, trusted base image
I used the python:3.11.8-alpine3.19 image with the up-to-date OS (security-wise) to mitigate the latest vulnerabilities.

## Simplicity
By not adding extra complexity to the Dockerfile, I reduce the attack surface.
