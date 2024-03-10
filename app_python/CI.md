# Continuous Integration Best Practices

This document outlines the best practices I implemented in the CI pipelines.

## 1. Set Timeouts for Workflows

To prevent workflows from running indefinitely, I set timeouts. This ensures
that if a step or a job hangs, it doesn't consume resources indefinitely.

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 20
```

## 2. Pin Actions to SHAs

For security reasons, I pin GitHub Actions to their SHA instead of using tags.
This ensures that we are always using the version of the action we expect. The
actions with ‘Verified creator’ badge on GitHub Marketplace are considered
trusted actions, thus its enough to specify a tag.

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v2 # trusted action
  - name: Setup Node.js
    # pinned to a SHA
    uses: actions/setup-node@210279a4c04a9b63dde5d0c8d8b31e8e8c5a1f23
```

## 3. Pin Test Runners to Version

I pin our test runners to a specific version instead of using the `latest` tag.
This ensures that our tests are always run in a consistent environment.

```yaml
jobs:
  build:
    runs-on: ubuntu-22.04
```

## 4. Concurrency Strategy

I use the concurrency strategy to ensure that only the latest commit is tested
when multiple commits are pushed in quick succession. This saves resources and
time.

```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true
```

## 5. Consider Which Triggers are Really Needed

I carefully consider which events should trigger the workflows. This prevents
unnecessary runs and saves resources.

```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
```

## 6. Use Caching

I use caching to speed up the workflows by reusing data from previous runs of
the same or similar jobs.

```yaml
steps:
  - name: Cache node modules
    uses: actions/cache@v2
    with:
      path: ~/.npm
      key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
      restore-keys: |
        ${{ runner.os }}-node-
```

## 7. Branch and Path Filters

I use branch and path filters to control when our workflows run. This ensures
that workflows only run when necessary.

```yaml
on:
  push:
    branches:
      - main
    paths:
      - 'src/**'
  pull_request:
    branches:
      - main
    paths:
      - 'src/**'
```

By following these best practices, I ensure that our CI/CD pipeline is
efficient, secure, and reliable.
