# Best practices used in 'Dockerfile'
Note there is no 'logs' implementation inside app, since docker already provides this feature via stdout.
## Using Official Base Image
Using an official Python runtime image as your parent image, which is recommended for stability and security.

## Setting Working Directory
Setting the working directory inside the container, which helps to organize files and commands within the container environment.

## Minimizing Dependencies
Minimizing the number of layers and dependencies by combining commands when possible, like updating apk and adding build tools in a single `RUN` command.

## Copying Necessary Files 
Only copying necessary files into the container, which helps reduce the image size and improves build efficiency.

## Giving Minimal Permissions
Giving minimal permissions by adding a dedicated user and group, and only providing ownership for the non-executable files, which enhances security.

## Exposing Necessary Ports
Explicitly exposing only the necessary port (port 5000) required for the application to communicate with the outside world.

## Running as Non-Root User
Running the application as a non-root user, which is a security best practice to minimize potential damage from security vulnerabilities.

## Using Entry Point Command
Using an entry point command to specify how the container should run by default, which enhances clarity and maintainability of the Dockerfile.

## Using stable precise version of base image
Using the exact image hash, so it will not be rebuilt

## Using Linter
I use [this linter](https://hadolint.github.io/hadolint/) to briefly check, if 'Dockerfile' has some problems

## ADD COPY
I avoided to use ADD command, used only COPY