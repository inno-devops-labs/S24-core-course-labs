# Date and Time in Moscow

## Table of Content

<!--toc:start-->
- [Date and Time in Moscow](#date-and-time-in-moscow)
  - [Table of Content](#table-of-content)
  - [Framework Choice](#framework-choice)
    - [Scope of Choice](#scope-of-choice)
    - [Flask](#flask)
    - [Django](#django)
    - [FastAPI](#fastapi)
    - [Why Flask](#why-flask)
  - [Best Practices](#best-practices)
  - [Unit Tests](#unit-tests)
<!--toc:end-->

## Framework Choice

Application is implemented using Flask framework and in the following section
you may see reasons of that

### Scope of Choice

According to the blog post [Django vs Flask: Which is the Best Python Web
Framework?](https://blog.jetbrains.com/pycharm/2023/11/django-vs-flask-which-is-the-best-python-web-framework/)
there are the following popular frameworks:

1. Flask
2. Django
3. FastAPI

Only popular frameworks are taken into consideration as they are widely used by
both small and large projects which gives us:

- Big community of developers using it
- Comprehensive documentation and a number of examples of how to use different
  features of the framework
- Adoption of most commonly used features (i.e. database drivers) via built in
  functionality or easy to integrate third party dependencies

### Flask

- **Type**: Microframework
- **Use Case**: Simple web applications, APIs, RESTful services, and prototyping
- **Strengths**: Lightweight, flexible, and provides more control over the architecture
- **Weaknesses**: Limited features out of the box, which may require additional libraries for certain functionalities

### Django

- **Type**: Full-stack web framework
- **Use Case**: Large, feature-rich applications such as e-commerce websites, content management systems, and social networking websites
- **Strengths**: Speed, security, and scalability
- **Weaknesses**: Can be less flexible compared to microframeworks, may have a steeper learning curve for beginners

### FastAPI

- **Type**: Modern API framework
- **Use Case**: High-performance APIs, machine learning, deep learning, and data-intensive applications
- **Strengths**: Based on Starlette and Pydantic, making it very fast and easy to develop APIs
- **Weaknesses**: May not be as suitable for full-stack development compared to Django

### Why Flask

This app uses Flask framework as it is a simple web application satisfies all the following criteria:

- Should be suitable for small applications
- Possibly lightweight
- Should support some kind of HTML templating as the application needs frontend
  page as well as backend server logic

## Best Practices

1. Following PEP 8 Style Guide:
   - Handled by Black formatter and Pyright language server
2. Graceful Exception Handling:
   - Exceptions that may occur are handled and logged
3. Logging:
   - All major events are logged
4. Testing
   - Due to non-functional nature of python it is impossible to write test which
     checks if function returning timezone works independently of timezone on
     host machine. Possible way to test this would be to change timezone of the
     machine (for e.g. it may be automated using Docker), however, it would be
     an overkill for the current case.
   - There isn't any important functionality to unit test except always getting
     date time in Moscow timezone and thus no unit tests were written
5. Typing:
   - All the functions and some variables are typed which not only makes it
     easier to understand their purpose, but also allows checking type
     correctness statically which leads to fewer bugs
6. `.gitignore` file uses [template recommended by GitHub](https://github.com/github/gitignore/blob/main/Python.gitignore)

## Unit Tests

Due to the simplicity of the application only a function `get_moscow_date_time`
is tested, but nonetheless it follows the next best practices:

1. **Isolating tests from external dependencies:** The use of
   `@patch('datetime.datetime')` replaces the actual `datetime.datetime` module
   with a mock version, allowing us to control its behavior during testing.
2. **Writing small, focused tests:** This single test focuses specifically on
   checking whether the returned timezone is correct and matches the expected
   value ('Europe/Moscow').
3. **Using descriptive names:** The name "test_moscow_time" makes it easy to
   identify the purpose of this particular test.
4. **Keeping tests independent:** Since each test runs independently, there is no
   dependency on the order in which these tests are executed.
5. **Consistent naming conventions**: Adheres to standard naming pattern of `test_*`.
6. **Document tests**: Briefly documents the intent of the test via clear commenting:
7. **Run tests frequently**: Executes tests upon changes within the `app_python`
   directory utilizing continuous integration (CI).
