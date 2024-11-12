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
- It is in the app_python directory, not in teh root.