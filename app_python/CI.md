# Docker

## Best practices

### Selective CI triggering

CI is only triggered if specific directories or files are changed - `app_python` or the workflow file itself. It prevents the redundant usage of the CI.

### Versions specification

I have specified the version tags that are used inside the CI to make sure it runs the same way every time.

### Use of Secrets

Sensitive data is stored inside the github secrets to avoid data loss.

### Setting timeouts

The timeouts are set to prevent the indefinite running of the action.

### Caching

I have used caching in `docker` step to reuse some data and make the process faster
