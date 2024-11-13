## Best Practices Applied in the Web Application

### 1. Modular Structure
The application follows a modular structure where each part of the web application is kept separate, making the codebase more maintainable and easier to extend. 

### 2. Clean Code and Readability
The code is written with readability in mind, following the **PEP 8** guidelines for Python. This ensures that the code is easy to read and understand by anyone working with it.

### 3. Code Commenting
The code is properly commented.
### 4. Dependency Management
The **`requirements.txt`** file lists only the required libraries. I used the **`pipreqs`** tool to automatically generate the list of dependencies, ensuring that only the libraries actually used in the project are included. This helps to keep the environment clean and avoids unnecessary dependencies.

### 5. Timezone Accuracy
The application uses the **pytz** library to accurately handle time.

## Coding Standards

### 1. PEP 8 Compliance with flake8
The code adheres to the **PEP 8** style guide, which is the standard for Python code. I used **flake8** as an error detection tool to check for code style violations.

### 2. Manual Testing/Debugging
Since the application is small at this stage, automated tests would be an overkill. I have performed manual testing and debugging to ensure that the displayed time updates correctly and the app behaves as expected. As the app grows, automated tests can be introduced to handle more complex scenarios.
