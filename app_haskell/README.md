# Current Moscow Time

[![Haskell web application][badge]][workflow]

[badge]: https://github.com/SnejUgal/S24-core-course-labs/actions/workflows/haskell.yaml/badge.svg

A simple web application that shows the current time in Moscow.

```
$ curl localhost:8081
2024-02-05T23:28:37.741671607+03:00
```

## Installation

Ensure that you have Haskell and Stack installed. After that, build the
application using `stack build`.

## Running

```bash
stack run
```

Now you can make requests to `localhost:8081` to fetch the current Moscow time.

## Docker

You can also use a Docker container with this app. If you want to build a new
image for this app, run

```bash
docker build -t devops-haskell .
```

Alternatively, you can pull an already-built image from Docker Hub. Download it
by running

```bash
docker pull snejugal/devops-lab2-haskell
```

Once you obtain the image, run it using

```bash
docker run --rm -p 8081:8081 snejugal/devops-lab2-haskell
```

## Testing

To run tests for the application, run `stack test`.

## CI

This reposity has a CI workflow which automatically runs tests for this
application and updates the app's image on Docker hub. See the [workflow] for
more.

[workflow]: ../.github/workflows/haskell.yaml
