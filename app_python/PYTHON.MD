# Lab 1

## Framework choice

I chose the minimalistic framework FastAPI because it is well-designed for small projects. It is easy to start a project
using [**FastAPI**](https://fastapi.tiangolo.com/). In our case with this framework we can put everything in one file
because we have a tiny codebase.

The other point is that we do not have any redundant parts of codebase with FastAPI, so it is much easier to analyze
comparing to **[Django](https://www.djangoproject.com/)** or **[Flask](https://flask.palletsprojects.com/en/3.0.x/)**.
Moreover, we do not need any separate services such as codebase. Therefore, the
configuration will be minimal.

## Testing

* ### Tests description
  I have created the unit tests for the testing the single endpoint of my application.
  I test several features of my response:
    * Status Code is valid
    * DateTime format is valid
    * DataTime timezone is Moscow timezone
    * The Moscow time corresponds to the NTP server time.

## Best practices

* ### Standards

  In my application I followed the standards of python code such as PEP8. I avoided all the code smells, followed the
  restricted length of lines up to 79 chars. I also documented my code properly.

* ### Linters

  For linting I used Pylint to ensure that my code follows the common best practices.

* ### Formatters

  For formatting, I used the Black and Isort to structure the code properly, follow the restricted length of lines and
  sort the imports.

* ### Tests
    1. #### Tests Should Be Fast
       The tests I wrote are fast and modulus. For example, test that checks the status code does not depend on test
       that checks the format of datetime.
    2. #### Tests Should Be Simple
       Tests are simple as possible. I tried my best to simplify each test and extract some logic into the functions if
       possible.
    3. #### Test Shouldn’t Duplicate Implementation Logic
       I did not duplicate any logic of the program in my tests.
    4. #### Tests Should Be Readable
       Tests are small, simple and well-documented. Therefore, they are readable for other developers.
    5. #### Tests Should Be Deterministic
       Tests are deterministic if they are run on modern hardware. This means that I have some simple tests that work
       with time and count on high precision of the application time comparing to NTP time.
    6. #### Make Sure They’re Part of the Build Process
       The tests are part of the build process in my pipeline.
    7. #### Distinguish Between The Many Types of Test Doubles and Use Them Appropriately
       I have no external dependencies. Therefore, I follow this practice anyway.
    8. #### Adopt a Sound Naming Convention for Your Tests
       All the tests names follow the same convention. The names describe the purpose of the tests.