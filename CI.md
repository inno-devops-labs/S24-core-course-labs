# Moscow time server CI best practices

## Github CI
Best practices applied:
- Docker Hub credentials stored in repository secrets
- Set custom timeouts that seemed appropriate for individual jobs
- Set only the `content: read` and `checks: write` permission for the workflow
- Pinned runners to `ubuntu-22.04`
- Pip and docker actions utilise github build cache
- Utilising snyk for code scans
