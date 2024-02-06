# Python web application

## Overview

This web application provides the current time in the Moscow time zone.

## Running application

1. Ensure you have `Python 3` installed by running:

   ```properties
   python --version
   ```

   or

   ```properties
   python3 --vresion
   ```

   Verify that the version is greater than or equal to 3.0.0.

2. Navigate to app_python.

3. Create and activate virtual evnironment.

4. Install requirements

   ```properties
   pip install -r requirements.txt
   ```

5. Start the application using:

   ```properties
   flask --app app run
   ```

6. Go to the link shown in the terminal, and you will get the time in Moscow.

## Testing

For testing purposes, you can execute all tests by running the following command inside the `/app_python` directory:

```properties
pytest
```
