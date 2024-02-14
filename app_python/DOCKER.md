# Lab 2: Docker Best Practices

## Using non-root user
Achieve security when the applincation in the image is running by non-root user

## Use Copy, but only specific files
Using the Copy instruction to copy specific files and directories into the container, reducing the image size.


## Layer sanity
Combine related commands to minimize the number of layers in the Docker image.

## Use a precise versions of base image
Use `python:3.10-slim` as base image as it is compatible with my application

## Create `.dockerignore` file
Create `.dockerignore` file to excluce unncessary files and directories from being copied.

