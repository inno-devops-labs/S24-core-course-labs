# Java Web Application

## Framework choice

Spring is the most famous, widely-used and developed framework for web development on Java.

## Best practices

Here I also follow KISS principle.
Code is formatted using IDEA formatter.

## Testing

This application was tested by opening service page with Moscow time in browser.

# Docker

## How to build Java Web Application image?

```bash
cd app_java
docker build -t masterlogick/devops-java-img .
```

## How to pull Java Web Application image?

```bash
docker pull masterlogick/devops-java-img
```

# How to run Java Web Application?

```bash
docker run -p 8080:8080 masterlogick/devops-java-img
```
