# Project Description

## Framework Selection

For the bonus task, I have picked Bun. Bun is a runtime for Javascript. I picked it instead of Node because Bun comes with preinstalled batteries (i.e. web server, testing, typescript support etc.). It is also faster than Node.

## Best Practices Followed

- Application routes and logics are separated into different modules.
- Typescript is used to ensure static typing.
- Prettifier is used to ensure unified coding styles.
- Unittests are maintained for the application.
- Linter is used to ensure better code quality.
- `package.json` to keep track of necessary packages.

## Ensuring Best Practices, Testing and Code Quality

- To have an unified coding styles, `prettier` was used
- To ensure better code quality, linter specs was defined in `tsconfig.json`
- Tests are written for every utility function using `bun:test` inside `app.test.ts`
- Documentation is maintained for all the functions and modules.

![Screenshot](https://i.postimg.cc/sD97G5cR/image.png)

## Unit Tests

The unit tests are maintained in `app.test.ts` file. Ideally it should be in a separate directory but because there are only 2 functions to test, only one file is maintained. Tests were not written for `app.ts` because that just wraps `returnTime` and `returnTime` is already tested. Also, testing `app.ts` falls under integration testing and not unit testing.
Several best practices were followed while writing the tests:

- Tests are fast and simple
- Each test works for individual functions
- All tests are deterministic
- Both positive and negative tests are maintained
- Code coverage is 100%. An [optimal code coverage is 75%-90%](https://testing.googleblog.com/2020/08/code-coverage-best-practices.html) but 100% is covered here due to the simplicity of the project.
