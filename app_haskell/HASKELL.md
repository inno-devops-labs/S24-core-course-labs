# Haskell Web Application

## Rationale for the web framework

I chose `servant` as the web framework for this app because it's a popular
framework in the Haskell ecosystem and I already had experience with it.

## Best practices

In my web app, I used these best practices:

- Separate the application into library and binary parts;
- Keep code as pure as possible, using the IO monad only for actual
  side effects.

In addition, I formatted my code using `brittany`. I also keep many compiler
warnings enabled to ensure code quality.

## Testing

The application is quite small, and `getCurrentMoscowTime` is the only
function one can write unit tests for (other tests would be integration tests).
For this function, I test these properties:

- The returned time is not too old;
- The timezone is correct;
- The returned time is monotonic.

While writing tests, I followed these best practices:

- Write tightly scoped unit tests;
- Check that the tests work by intentionally introducing a bug.
