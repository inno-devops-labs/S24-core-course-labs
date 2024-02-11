# Docker

## Best practices

- The container does not run under `root`, but it uses specially created group and user
- Official Python image was used
- The base image version was clearly stated: `python:3.12-alpine3.18`
- Only `8080` (required for app) port is exposed
- Dependencies are installed before the application files are copied, so they would not be reinstalled on code changes
- Only `app` folder and `requirements.txt` are copied inside the image
- `Dockerfile` was checked using `hadolint`
