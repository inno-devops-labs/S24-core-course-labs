# Python Web Application: Moscow Time Display

## 📌 Description

This Python web application is built using the Flask framework to display the current time in Moscow. The application separates the date and time, ensuring accurate timezone handling through the `pytz` library.

## 📎 Project Structure
```
├── app_python
│   ├── app.py
│   ├── templates
│   │   ├── index.html
│   ├── static
│   │   ├── moscow.jpg
│   ├── PYTHON.md
│   ├── README.md
│   ├── requirements.txt
```

## ✅ Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
## ✨ Usage
1. Run the Flask application:

   ```bash
   python app.py
   
2. Open your web browser and navigate to http://127.0.0.1:5000/ to view the application.

## 🎉 Features

**🕐 Displays the current date and time in Moscow.**

**🏙️ Uses a background image from the static folder.**

**⚡️ Basic error handling for unexpected situations.**

## 👍🏻 Best Practices and Code Quality

1. Follows the principle of separation of concerns.
2. Adheres to PEP 8 coding standards for clean and readable code.
3. Implements basic error handling to ensure graceful degradation.
4. Includes functional testing for the main application.

## ⚡️ Dependencies

1. Flask
2. pytz

##🚀 Dockerized Application
####1. Build the Docker Image
To build the Docker image for this application locally, use the following commands:
```
# Build the Docker image
docker build -t flask-moscow-app .
```

Alternatively, you can pull the Docker image from Docker Hub:
```
# Pull the Docker image from Docker Hub
docker pull nytakoe115/flask-moscow-app
```

####2. Run the Docker Container
Once you have the Docker image, run the Docker container with the following command:
```
# Run the Docker container
docker run -p 4000:80 flask-moscow-app
```
If you pulled the image from Docker Hub, use the following command:
```
# Run the Docker container
docker run -p 4000:80 nytakoe115/flask-moscow-app
```

####3. Access the Web Application
Open your web browser and navigate to http://localhost:4000 to view the Moscow Time web application.

## 📚 Acknowledgments

1. [Flask](https://flask.palletsprojects.com/)
2. [pytz](https://pythonhosted.org/pytz/)

## 🩷 Thank you!
Feel free to customize this template with additional sections or information specific to your application.