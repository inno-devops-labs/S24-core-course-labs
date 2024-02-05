# Java Web Application

## Framework Choice: Spring Boot

I chose to use the Spring Boot framework for this Java web application for the following reasons:

- **Robustness**: Spring Boot provides a comprehensive ecosystem with built-in features for web development, making it suitable for building robust and scalable applications.
- **Convention over Configuration**: Spring Boot follows the principle of convention over configuration, reducing boilerplate code and allowing developers to focus on business logic.
- **Integration**: Spring Boot seamlessly integrates with other Spring projects and third-party libraries, offering a wide range of functionalities.

## Additional Notes

- The application tracks how many times a specific route is accessed using a simple counter mechanism implemented in the controller.
- The code follows best practices and coding standards recommended for Spring Boot applications.

## Best Practices Applied

1. **MVC Architecture**: The application follows the Model-View-Controller (MVC) architectural pattern, separating concerns and improving maintainability.

2. **Dependency Injection**: Spring Boot's dependency injection feature is utilized to manage dependencies and promote loose coupling between components.

## Coding Standards

1. **Camel Case**: Variable and method names follow the camel case convention for improved readability.

2. **Comments**: Comments are used to explain complex logic and provide clarity where necessary.

## Testing

**Unit Testing**: Unit tests are implemented using JUnit and Mockito to verify the functionality of the controller method that increments the access count.
