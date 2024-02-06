# Python time app

The application is showing the current Moscow time that updates upon page reload.

# How to run
1. Install all requirements from requirements.txt using the following command (either inside venv or in global env):
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app using the following command (assume that the current directory is app_python)
   ```bash
   python api/main.py
   ```

# Testing
Unit and manual testing are used to ensure corectness of the application. 

Manual testing scenario was to refresh the page and check time is changed.

The unit testing part contains test for checking the correctness of the function that provides formatted time information. (With mocked time)

To run unit test use the following command:
```bash
pytest
```
