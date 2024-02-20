# Flask Time Zone Web App 🌐⏰

📄 **Description:**
This project is a simple web application built using Flask, a Python web framework. The app displays the current time in GMT+3 (Moscow time zone) and updates it on page refresh. 

🛠️ **Tech Stack:**

- Flask
- HTML, CSS

👩‍💻 **Key Features:**

- Real-time display of current time in GMT+3
- Time updates on page refresh for user convenience

🚀 **Best Practices Applied:**

- Code structured following Flask conventions
- HTML templating for separation of concerns
- Timezone handling using **`pytz`**
- Font customization through CSS
- Page refresh time update
- Follows code cleanliness with no unused imports

🧪 **Testing Instructions:**

1. Clone this repo and navigate to **`app_python`** folder
2. Install required dependencies (**`pip install -r requirements.txt`**)
3. Run the Flask application (**`python app.py`**)
4. Open a web browser and navigate to **`http://127.0.0.1:5000/`**
5. Observe the real-time display of the current time in Moscow (GMT+3)
6. Refresh the page to get the current time

🐳 **Docker:**

To run the application in a Docker container, follow these steps:

1. Build Docker Image:
**`docker build -t flask-app .`**

2. Run Docker Container:
To run the Docker container, execute the following command:
**`docker run -p 5000:5000 devops-lab`**

3. Pull Docker Image:
**`docker pull nikzor/flask-app`**

3. Run Docker Container:
**`docker run -d -p 5000:5000 flask-app`**

Access the application at **`http://127.0.0.1:5000/`** in your web browser.

⚙️ **Unit Tests**

Unit tests ensure the correctness and reliability of the application's functionality. The tests cover critical components and behaviors, providing confidence in the codebase. Below are the unit tests applied to this project:

- **test_get_current_time_format**: This test verifies that the `get_current_time` function returns the current time in the correct format (HH:MM:SS).

To run the unit tests, execute the following command in your terminal:

**`pytest`**
