# Framework Choice and Best Practices

## Framework
Flask was chosen as it is a lightweight Python framework, making it ideal for building small to medium-sized web applications 
like this one. 

I was choosing between **FastAPI** and **Flask** as they are both
good for fast and optimized solutions, but I'd chosen to stick with **Flask** to create nice and simple UI using 
its built-in Jinja2 templating engine

## Best Practices
 
* Project Layout: The application has clear and organized code structure that can be simply expanded, with separate modules and the use of application factory pattern.
* Effective use of templates: Flask supports the use of Jinja2 templates for rendering dynamic content. It helps to separate the application logic from the presentation layer, using template inheritance to avoid code duplication.
### Testing
For testing, `pytest` framework is used to implement simple unit-tests for checking the time and page rendering correctness.
`pytest.fixture` class is used to conveniently reuse `test_client` instance among all running tests.

You can run those tests by executing the command
```sh
(venv) $ python -m pytest -v
```