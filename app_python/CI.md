# CI

## Practices used

1. Dependency caching via option of setup-python (see
   [link](https://github.blog/changelog/2021-11-23-github-actions-setup-python-now-supports-dependency-caching/))
2. Multiple version of Python in testing
3. Push to DockerHub only when necessary - after merging in main
4. Separated workflows
5. Workflow results visible as badge
6. Using some of the latest versions of actions
7. Run only on changes withing app_python folder