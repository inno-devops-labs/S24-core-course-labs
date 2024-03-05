# CI

---

## Used Best Practices

1. Secrets are stored in GitHub Secrets of repository
2. Set small timeout for workflow (30 minutes)
3. All uses are pinned to commit (for example, `actions/checkout@f43a0e5ff2bd294095638e18286ca9a3d1956744`)
4. Pinned test runners to version (for example, `ubuntu-22.04`)
5. Caching dependencies to increase build speed

[//]: # (Source of Best Practices: https://exercism.org/docs/building/github/gha-best-practices)

[//]: # (Caching dependencies to increase build speed: https://github.com/actions/cache?tab=readme-ov-file#creating-a-cache-key)