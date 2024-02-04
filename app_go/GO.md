# Best Practices Applied in the Web Application

## Dependency Injection: 
The application utilizes dependency injection for the clock service, allowing for easier testing and decoupling of components.

## Graceful Shutdown: 
The application handles graceful shutdown by listening for SIGTERM and SIGINT signals, ensuring that active connections are properly closed before exiting.

## Configuration Management: 
The application allows configuring the server address via environment variables, providing flexibility and ease of deployment.

## Error Handling: 
Errors are properly handled and logged, providing visibility into potential issues during runtime.

## Logging: 
The application uses the zerolog library for logging, allowing for structured logging and better insight into application behavior.

## Linters
The application code was checked with set of linters from `golangci-lint` (https://golangci-lint.run/)

## Coding Standards and Code Quality
### Code Formatting: 
The code follows the standard Go formatting conventions, ensuring consistency and readability.

### Error Handling: 
Errors are handled appropriately using idiomatic Go error handling techniques, improving code reliability and maintainability.

### Testing: 
The application includes unit tests for critical components such as the clock service and HTTP handlers. Testing is an integral part of the development process, ensuring that the application behaves as expected under different scenarios.

### Documentation: 
Code is appropriately documented with comments, providing context and guidance for future maintainers.

### Code Reviews: 
Code reviews are conducted to ensure code quality, adherence to coding standards, and proper implementation of features.