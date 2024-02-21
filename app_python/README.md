# Python Web Application - Current Time in Moscow

## Description
This Python web application displays the current time in Moscow. It is a simple Flask application that fetches the current time in the Moscow timezone using the datetime and pytz libraries.

## Installation
1. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```
2. Install the required dependencies using the requirements.txt file:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application by executing the following command in your terminal:
   ```
   python app.py
   ```
2. Access the web application in your browser at http://localhost:5000/ to view the current time in Moscow.

## App.py Code Explanation
1. The code fetches the current time in Moscow timezone using the pytz library.
2. If successful, it returns the current time in Moscow as a response.
3. If an error occurs, it returns an error message.

## Error Handling
The application includes error handling to manage exceptions and provides an error message if any issues occur.

## .gitignore
The .gitignore file is included to ensure that unnecessary files and directories are not pushed to the repository.

## requirements.txt
The requirements.txt file lists the necessary dependencies for the application to function correctly.

## Technologies Used
- Python
- Flask
- pytz
- datetime