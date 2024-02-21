# Visual Sorts

## Framework Choice

This web-application is built with [Svelte](https://svelte.dev/) — compiler that converts declarative components into efficient JavaScript.

I've chosen Svelte, because it was my pet project and I was interested in
learning a new popular JavaScript tool.

## Best Practices

When implementing the web application, I followed the best practices:

- I created a `package.json` where I listed all project requirements and dev-requirements separately;
- I followed [Svelte documentation](https://svelte.dev/docs/introduction), when implementing the app;
- I splitted app into several components to make code reusable and maintainable;
- In JavaScript has no common coding-style standard like PEP8 in Python, but my own style is consistent accross the codebase;

I also manually tested the application locally on my machine.

## Unit Tests

Application unit tests are located in `src` and names like `*.test.ts`.

- I followed official Vitest guidelines on how to write the tests (de-facto in JS).
- I used multiple small unit tests to test only specific functions to make sure they work as expected.
