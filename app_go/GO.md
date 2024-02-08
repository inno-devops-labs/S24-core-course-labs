# Cat facts app

## Framework

The standard-library framework is used for the web app, as it
is capable enough for this simple app and does not require an
external installation.

## Best practices

-   The code is logically distributed into files.

-   The code is written in clean Go, according to the Go guidelines.

-   To ensure project quality, I used the built-in `go vet` static
    analysis tool and manually run the application.

-   Explicit error handling is applied everywhere except for transmission
    errors (both in networking and when printing to console), which are
    explicitly ignored for there is nothing to do in those cases.
