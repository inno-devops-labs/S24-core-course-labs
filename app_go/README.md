# Cat fact web app

A web application that shows random cat facts on its main page.

## One-shot run

In the project directory run `go run .`. That's it!

Note that it requires the go module support (on by default in modern versions
of go, on an old version enable manually with the `GO111MODULE=on` environment
variable).

## Compile and run

In the project directory run `go build .`. This will create an executable file
`catfact_webapp`. Run it to start the web app.

## Docker

To build, in the project directory do:

```bash
docker build . -t IMAGE_TAG_NAME
```

where `IMAGE_TAG_NAME` is the tag you want for the image.

### Pull

You can also run a pre-built version of the image. To pull it:

```bash
docker pull kolay0ne/app_go
```

Use `kolay0ne/app_go` as the image name for future docker operations.

### Run

Run a container based on the image, select options depending on your needs. For
instance, to run it in the background, exposing the port `5000` to a randomly
selected port on the host machine and automatically remove the container ones
it's stopped, do: 
```bash
docker run --rm -d -p 5000 kolay0ne/app_go
```

Replace `kolay0ne/app_go` with your image/tag name if you built it manually.
