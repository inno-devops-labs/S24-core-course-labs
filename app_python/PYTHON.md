# Python Web Application

## Framework Choice: Flask

For this Python web application, I chose Flask as the web framework. Flask is a lightweight and flexible micro-framework that is ideal for simple web applications like this one.

## Implementation Details: Check the README.md file

## Best Practices

1. **Coding Standards:** The code follows basic coding standards such as consistent indentation and clear variable naming, adhering to Python's PEP 8 guidelines.

2. **Modularity:** ensured modularity by separating the application logic into different files, such as `app.py` for the main application code and `requirements.txt` for managing dependencies.

3. **Code Quality:** The code is concise and straightforward, focusing on the core functionality of displaying the current time in Moscow. However, additional comments and documentation could enhance readability and maintainability.

## How To Install and Test

To run the Flask web application, follow these steps:

2. **Create a Virtual Environment:**

   - It's recommended to use a virtual environment to isolate project dependencies. Create a new virtual environment by running:

     ```
     python -m venv venv
     ```

   - Activate the virtual environment:

     - On Windows:

       ```
       venv\Scripts\activate
       ```

     - On macOS/Linux:

       ```
       source venv/bin/activate
       ```

3. **Install Dependencies:**

   - Once the virtual environment is activated, install the required dependencies by running:
     ```
     pip install -r requirements.txt
     ```

4. **Run the Application:**

   - After installing dependencies, navigate to the directory containing the `app.py` file.
   - Run the following command to start the Flask development server:
     ```
     python app.py
     ```

5. **Test:**

   - Open a web browser and visit `http://127.0.0.1:5000/` to access the application.
   - You should see the current time in Moscow displayed on the webpage.
   - Refresh the browser tab and still works :)

   !["Website screen"](./screenshots/test.png)
   !["Website screen"](./screenshots/terminal.png)
