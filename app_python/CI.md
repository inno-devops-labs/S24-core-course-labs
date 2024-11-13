# CI Best Practices

## Workflow nuances
- Different jobs for different stages.
- Usage of needs:

## Tests
- Standard pytest unit testing with assertion.

## Linter
- Used GitHub Actions template to enforce PEP 8 codestyle.

## Caching
- Used template from GitHub Actions to cache dependencies.

## Security Checks
- SNYK with GitHub secrets to pass api key.

## Docker Integration
- CI Builds and pushes the image, used github secrets to pass credentials.

## CI Badge.
- Even two, one in root, one in app_python.