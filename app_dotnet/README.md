# CSharp web application

## Overview

This application gives you a string to help you to decide if you want to do something or not. Similar to head or tails.

## Running application

1. Ensure you have `dotnet` installed, you can check it using:

   ```properties
   dotnet --version
   ```

   You should see a version greater than or equal to `8.0.0`

2. Navigate to app_dotnet.

3. Trust the HTTPS development certificate by running the following command:

    ```properties
    dotnet dev-certs https --trust
    ```

4. navigate to `App`

5. Start the application using:

   ```properties
   dotnet run --launch-profile https
   ```

6. Go to the link shown in the terminal.

## Unit tests

For testing you can run all tests using

```properties
dotnet test
```

Inside `/app_dotnet` directory.

## Testing best practices

- All tests are isolated from each other. Thus, having a completly isolated unit testing.

- Followed Arrange, Act, Assert pattern (also known as AAA)

- Added docstring description for each test

- Followed common naming conventions for naming tests.


## Docker

### Pull

Run the following command to pull docker image from docker hub

```properties
docker pull ahmadalhussin/app_dotnet:latest
```

### Build

Run the following command to build docker image

```properties
docker build --tag ahmadalhussin/app_dotnet .
```

### Run 

To start the image

```properties
docker run -d -p 8080:8080 ahmadalhussin/app_dotnet
```

## CI

For Continuous Integration I created multiple yml files in `.github/workflows/` directory.

For each one, multiple parts are being runned to achieve the desired goal.

The first part is to build the application. This stage consist of the following:

- Install dependencies

- Running unit tests

- Linting/building project

The next part is to push our docker image to docker hub. This part is divided also to:

- Login to docker hub using GitHub secrect

- Build Image

- Tag the Image

- Push the image to docker hub
