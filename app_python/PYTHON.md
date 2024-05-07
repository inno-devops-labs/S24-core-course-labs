# Python application

This document describe the structure of a web application written in python.

## Framework chosen

Flask is used as the main web framework for the application.

### Reasons behind choosing flask

1. **High scalability**: Since this course is designed in a way where each lab builds upon the previous one. It is neccessary to choose a framework that scale easily.

2. **Easy to use**: Flask, unlike many other frameworks is so easy to setup and use.

3. **Popularity**: Flask is one of the most frameworks for python. It is important in order to find support for different problems in future.

## Best practices, and how I used them

1. **Project structure**: In this application I followed the project layout specified in the [official docs](https://flask.palletsprojects.com/en/3.0.x/tutorial/layout/#project-layout).

2. **Format**: In this project all the code is fomatted using black formatter

3. **Documenting code**: All functions in the project are documented following the docstring documentation.

## Testing

I wrote tests for the main endpoint, the following tests where added:

1. Test the availability of the endpoint.

2. Test the correctness of the time displayed.

3. Test how refreshing the page affects the time diplayed.

## Testing best practices

- All tests are isolated from each other. Thus, having a completly isolated unit testing.

- Followed Arrange, Act, Assert pattern (also known as AAA)

- Added docstring description for each test

- Followed common naming conventions for naming tests.

## Ensure code quality

I formatted the code using python black formatter

```properties
black file_name.py
```
