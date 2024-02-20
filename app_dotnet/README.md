# CSharp web application

## Overview

This application gives you a string to help you to decide if you want to do something or not. Similar to head or tails.

## Running application

1. Ensure you have `dotnet` installed, you can check it using:

   ```properties
   dotnet --version
   ```

   You should see a version greater than or equal to `8.0.0`

2. Navigate to app_cs.

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

## Testing

For testing you can run all tests using

```properties
dotnet test
```

Inside `/app_cs` directory.
