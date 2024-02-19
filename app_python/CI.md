# CI best practices

CI triggers only if the change wass occured inside `app_python/` directory

## Automated build and test processes

Workflow contains Pytest and Docker stages, where pytest runs unit tests and after successful passage, docker builds and pushes the iage

## Code reviews and quality checks

There is another workflow which checks for properly formatted code

## Integration with issue tracking and project management tools

For this practice, Snyk tool was integrated to check for vulnerabilities and report to the dashboard.
