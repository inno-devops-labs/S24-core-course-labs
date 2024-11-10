# Python application for displaying Moscow time

## Web framework

For this assignment I chose Flask web framework because it offers a clean and easy interface and does not bloat the code while also packing more than enough for completing the task.

## Best practices

I tried to name my variables according to the semantics and I also offer a fallback in case something goes wrong.

## Testing

I used manual testing to ensure quality.

## Unit tests

In order to automatically check if the application could successfully be deployed (e.g. no syntax/runtime errors), the application is covered with unit tests.

I decided to only perform [black box testing](https://en.wikipedia.org/wiki/Black-box_testing) to ensure that the system as a whole works as intended, and not just particular components such as functions.

The tests are located in `tests/` folder, and right now contain one unit test.

The test will perform HTTP request to the server and ensure that it does indeed return time in specified format.

