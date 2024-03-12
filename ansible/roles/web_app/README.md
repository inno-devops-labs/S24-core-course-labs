# Web app run role

This role starts docker container with web app and opens one port from container.

## Requirements

+ Ubuntu
+ Docker (you could use `docker` role to install it)

## Usage

```
    - role: web_app
      become: yes
      vars:
        app_directory: app_java
        app_image: masterlogick/devops-java-img
        app_port: 8080
```