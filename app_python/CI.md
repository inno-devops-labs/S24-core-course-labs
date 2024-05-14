## CI best practice on Github Actions

### Managing GitHub Actions Secrets

I used GitHub Secrets to set docker hub username and access token in privet. so CI workflow still have it as
environmental variable, but they are not visiable on the github.

### Caching

I used cache to optimise testing and linting in term of time. It passes much faster when we have cached requirements.
