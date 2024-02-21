# Visual Sorts

![Tests workflow](https://github.com/evermake/iu_devops/actions/workflows/ci-javascript.yaml/badge.svg)

## Overview

Web-application written in [Svelte](https://svelte.dev) and [TypeScript](https://www.typescriptlang.org/) that visualizes common sorting algorithms.

## Online Demo

[evermake.github.io/visual-sorts](https://evermake.github.io/visual-sorts)

## Local Setup

_Step 1._ Install [NodeJS v18+](https://nodejs.org/en).

_Step 2._ Install [pnpm](https://pnpm.io/installation).

_Step 3._ Open the `app_javascript` directory and run commands below from there.

_Step 4._ Install dependencies:

```sh
pnpm install
```

_Step 5._ Run local development server:

```sh
pnpm run dev
```

_Step 6._ Go to [localhost:5173](http://localhost:5173) in the browser and watch sorting algorithms in action.

_Step 7._ (Optional) To build the production build run:

```sh
pnpm run build
```

Production build will be in `dist` directory.

## Docker

### Building image

To build image, use the following command (substitute `x.y.z` with the actual version):

```sh
docker build -t devops-visual-sorts:x.y.z .
```

### Pulling image from Docker Hub

Docker image is available on Docker Hub, to pull it use the following command:

```sh
docker pull evermake/devops-visual-sorts:latest
```

### Running container

To run the container, use the following command:

```sh
docker run -p 8000:8000 evermake/devops-visual-sorts
```

App will be available at [localhost:8000](http://localhost:8000).

## Testing

Tests are written with Vitest testing framework.

To run the tests, use the following command:

```sh
pnpm run test
```

## CI/CD

Application has a configured GitHub Actions workflow at root of the repository at `/.github/workflows/ci-javascript.yaml`, which includes:

- Running unit tests;
- Running checks with `svelte-check`;
- Building and publishing Docker image (if all checks above have passed).
