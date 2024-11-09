# Python Development

## Why Flask?
Flask is ideal for this project because it’s lightweight, easy to set up, and well-suited for small, dynamic applications. Its simplicity allows us to quickly render content, with minimal code. The built-in templating engine makes it easy to manage dynamic HTML, while Flask’s flexibility means we could expand the app.

## Best Practices Applied
1. Separation of Concerns: The application keeps logic and structure simple, focusing on clear routing (@app.route('/')) and using Flask’s render_template_string to separate HTML content from logic.
2. Environment Management: A virtual environment is used to isolate dependencies, ensuring compatibility and preventing conflicts with global packages.
3. Static File Management: The image is stored in the /static folder, following Flask’s convention for static assets, which improves scalability and organization.

## Code Quality
Minimal dependencies and concise code enhance maintainability, and the application’s small footprint reduces the chance of bugs.

## Unit Testing
Follow `/tests/test_app.py` to see the tests.

### `test_home_status_code`
- Verifies that the home page (`/`) loads successfully by checking for a status code of 200.
- Ensures the main route is functional and that users can access the application without errors.

### `test_home_content`
- Checks that the home page contains the title "Current Time in Moscow" to confirm that the content renders as expected.
- Ensures the displayed content includes the current time, formatted correctly, which is dynamically generated based on Moscow's timezone.

### `test_moscow_image_display`
- Confirms that the Moscow image is present on the home page by checking for the `<img>` tag with the correct source.
- Verifies that static assets are loaded correctly and displayed to the user, enhancing the application’s visual layout.

### `test_static_image_access`
- Tests direct access to the static image file (`/static/moscow.jpg`) by checking for a 200 status code.
- Ensures the image is served with the correct MIME type (`image/jpeg`), verifying that static files are accessible and properly formatted.