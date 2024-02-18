# CI

## Best practices

- Shorter timeout on workflows (20 min)
- Dockerhub token and username are contained in `GitHub Secrets`
- Workflow uses a precise version of runner (`ubuntu-22.04`)
- Dependency caching is enabled in `actions/setup-python@v4`
