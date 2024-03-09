# Dockerized web app deploy role

An ansible role for deploying a dockerized web app.

## Requirements

This role depends on the `docker` role from the same repository. No additional
requirements are imposed.

## Usage

All parameters of the role are optional. The most basic usage:
```
roles:
  - name: "Deploy hello-world"
    role: web_app
```
The above will pull the `hello-world` image tagged `latest`, create a container
`hello-world-0` corresponding to it, and start it.

The most advanced usage:
```
roles:
  - name: "Deploy asciiquarium"
    role: web_app
    image_name: "danielkraic/asciiquarium"
    image_tag: "master"
    container_name: "aq"
    publish_ports:
      - 5000:6000
      - 7000
    wipe: false
```
The above will pull the `danielkraic/asciiquarium` image tagged `master`, create
a container `aq` corresponding to it, and start it. The container's port `6000` will
be mapped to host `5000` and container's port `7000` will be mapped to an arbitrarily
selected host port.

Changing the `wipe` parameter to `true` (or another value that represents a boolean true
according to ansible) causes the container to be destroyed and the pulled image to be
removed from the managed machine. When `wipe` is `true`, the value of `publish_ports` is
ignored.
