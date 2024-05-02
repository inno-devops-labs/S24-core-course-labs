# CI for `app_python`

## Best practices

-   Runs on push only if files in related directories have changed.

-   Uses matrix strategy: runs tests with different python versions,
    can be extended further, e.g., to use different operating systems.

-   In the lint&test job, dependencies are cached and reused. Cache is
    updated when newer versions of dependent libraries are released.

-   In the docker build&push job, docker layers are cached and reused.
    Cache is updated when any of the layers change.
