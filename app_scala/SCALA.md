# Date and Time in Moscow

## Table of Content

<!--toc:start-->

- [Date and Time in Moscow](#date-and-time-in-moscow)
  - [Table of Content](#table-of-content)
  - [Tech Stack Choice](#tech-stack-choice)
  - [Best Practices](#best-practices)
  <!--toc:end-->

## Tech Stack Choice

- [Scala](https://www.scala-lang.org/) is a modern functional programming language with strong type system
- [ZIO](https://zio.dev/) is a powerful library for building concurrent and asynchronous
  applications in Scala. It allows developers to write code that is highly
  testable, resilient, and expressive.
- [Tapir](https://github.com/softwaremill/tapir) is a library which brings type
  safety to endpoint description
- [Vert.x](https://vertx.io/) as a backbone for HTTP server. It is
  resource-efficient and well-suited for asynchronous and concurrent applications

## Best Practices

1. Following Scala's official Style Guide:
   - Handled by Scalafmt formatter
2. Graceful Exception Handling:
   - Due to functional nature of Scala and type-level error handling of ZIO all
     errors are handled
3. Logging:
   - As ZIO provides its logging mechanisms, it is used in this app. It not only
     allows to easily change format of the logs, but also formats already
     defined logs (ones from third-party libraries)
4. Testing
   - ZIO allows for easy testing. For e.g. tests that check implementation of
     `getCurrentTime` in `MoscowDateTime` is easily tested by using custom
     instance of `Clock` which mocks real-world clock that is used during
     runtime
5. Typing:
   - Scala is strongly typed language. Moreover, its type system is very rich
     which allows developers to be sure in the correctness of the application
6. `.gitignore` file uses [template by author of Scala
   Cookbook](https://alvinalexander.com/source-code/scala/sample-gitignore-file-scala-sbt-intellij-eclipse/)

## Unit Tests

Due to the simplicity of the application only a function `MoscowDateTime.getCurrentTime`
is tested, but nonetheless it follows the next best practices:

1. **Isolating tests from external dependencies:** Due to functional nature of
   scala and ease of use of ZIO Test framework it is simple to mock all the
   outer world (including Clock service) for proper testing.
2. **Writing small, focused tests:** There are 2 test cases: whether the
   function returns time different to one in the timezone other than Moscow
   (London) is chosen and whether it returns the same time as in Moscow.
3. **Using descriptive names:** The name "Moscow Time Spec" encapsulates all the
   tests related to `MoscowTime` class
4. **Keeping tests independent:** Since each test runs independently, there is no
   dependency on the order in which these tests are executed.
5. **Consistent naming conventions**: Adheres to standard naming conventions of
   Scala and ZIO test
6. **Document tests**: Each test has a brief description on which feature it
   tests
7. **Run tests frequently**: Executes tests upon changes within the `app_scala`
   directory utilizing continuous integration (CI).
