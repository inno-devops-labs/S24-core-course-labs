# Python Web Application

This Python web application displays the current time in Moscow.

## Installation

1. Clone this repository to your local machine:

2. Navigate to the `app_python` directory:

    ```bash
    cd app_python
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application

1. Ensure you are in the `app_python` directory.

2. Run the application using the following command:

    ```bash
    python3 app.py
    ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/` to view the current time in Moscow.

### Running the Tests

1. Ensure you are in the `app_python` directory.

2. Run the test suite using the following command:

    ```bash
    python -m unittest test_app.py
    ```

3. After running the command, you should see the output of the test results.

## Technologies Used

- Python
- Flask
- pytz