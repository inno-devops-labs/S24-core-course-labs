# Implemented CI best practices

- Use new version of the actions (e.g. actions/checkout@v4, actions/setup-python@v5)
- Use dependencies caching ("cache: 'pip'" in actions/setup-python@v5)
- Only run build if the linting and tests succeed (needs)
- Testing, Linting, Vulnerability check (doesn't work)
