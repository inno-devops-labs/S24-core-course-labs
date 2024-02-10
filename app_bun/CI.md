# CI Description

A CI workflow is maintained in the `.github/workflows/build-bun.yaml` file. This workflow lints and tests the application, checks code vulnerability using SNYK, and builds and pushes docker image. Workflow is triggered only if the there is a change in the `app_bun` directory or the workflow file itself.

The workflow runs on the `ubuntu-22.04` runner and `bun 1.0.11` is used as the language.

In most cases, official actions are used where possible. But for `security` job it was not possible because SNYK requires the project to be in root directory. Since the python project is in the `app_bun` directory, I had to write custom actions for the `security` job.

## Jobs

There are 3 jobs in the workflow:

- Build
- Security
- Docker

`build` job lints and tests the application. If linting is not successful, job still continues to test the application. If tests are not successful, the job fails.

`security` job checks code vulnerability using SNYK. If the job is not successful, the workflow is stopped. This job fails only if a high or critical severity vulnerability is found.

`docker` job builds and pushes the docker image to the Docker Hub. The job is carried out only if the previous jobs are successful. As in, if all tests pass and no high severity vulnerabilities are found, the docker image is built and pushed to the Docker Hub.

## Best Practices

- The workflow is triggered only if the there is a change in the `app_bun` directory or the workflow file itself. This is to avoid unnecessary workflow runs.
- Caching is used to speed up the workflow. For example, the `build` job caches the python packages to avoid re-downloading them when `bun install` is executed. Similarly, the Snyk CLI is cached to avoid re-downloading it every time the `security` job runs.
- The actions are made to fail fast. For example, tests are run earlier so that the whole process halts if the tests fail.
- The workflow is made to be as parallel as possible. For example, the `build` and `security` jobs run in parallel. This is to save time and resources. However, the docker job is not run in parallel because we don't want to build and push the docker image if the tests or security checks fail.
- Time limits are set for jobs.
- OS version and python version are specified in the workflow file.
