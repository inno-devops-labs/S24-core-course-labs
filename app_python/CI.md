# CI best practices

## Parallel jobs

The workflow defines jobs that can run in parallel, maximizing efficiency and reducing overall workflow execution time.

## Cache Dependencies

Dependencies are cached using the `actions/cache` action, which helps speed up subsequent workflow runs by reusing
dependencies stored in the cache.

## Environment Variables/Secrets

Environment variables and secrets are used to provide sensitive information like Docker Hub credentials (${{
secrets.DOCKERHUB_USERNAME }} and ${{ secrets.DOCKERHUB_TOKEN }}) without exposing them in the workflow file.
