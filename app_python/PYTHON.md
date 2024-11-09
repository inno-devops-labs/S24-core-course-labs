## Why Flask?
Flask is ideal for this project because it’s lightweight, easy to set up, and well-suited for small, dynamic applications. Its simplicity allows us to quickly render content, with minimal code. The built-in templating engine makes it easy to manage dynamic HTML, while Flask’s flexibility means we could expand the app.

## Best Practices Applied
1. Separation of Concerns: The application keeps logic and structure simple, focusing on clear routing (@app.route('/')) and using Flask’s render_template_string to separate HTML content from logic.
2. Environment Management: A virtual environment is used to isolate dependencies, ensuring compatibility and preventing conflicts with global packages.
3. Static File Management: The image is stored in the /static folder, following Flask’s convention for static assets, which improves scalability and organization.

## Testing
The application was manually tested in a local development environment, confirming the correct display of the current time and image. Testing ensures that the app runs as expected and meets initial requirements.

## Code Quality
Minimal dependencies and concise code enhance maintainability, and the application’s small footprint reduces the chance of bugs.