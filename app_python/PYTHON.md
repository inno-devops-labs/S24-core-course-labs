# Moscow time web app

## Framework choice

For this app implementation I chose Flask. It is fairly simple,
especially for minimalistic apps, but, using other tools, can be
deployed in a rather advanced way.

## Best practices

-   The code is logically distributed into files,

-   The code is written in clean Python, follows PEP-8 guidelines,
    general-purpose functions are documented with docstrings,
    type hints are available where applicable.

-   To ensure the project quality, I used online tools for code
    quality evaluation, manually tested functions, and ran the
    web application and tested it in the browser by manually
    refreshing the page, carefully reading the response, and making
    sure it corresponds to moscow time.

-   The document does not rely on either local time zone (as it may
    be set to one other than Moscow) or local time (as it may be
    arbitrary), instead, it uses an external service as the source of
    truth.
