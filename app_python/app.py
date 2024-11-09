from flask import Flask, render_template_string
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def show_moscow_time():
    # Get the current time in Moscow
    moscow_time = datetime.now(pytz.timezone("Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")
    
    # Define HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Current Time in Moscow</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
            }
            .time-container {
                text-align: center;
            }
            h1 {
                font-size: 2rem;
                color: #333;
            }
            img {
                max-width: 600px;
                height: auto;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="time-container">
            <img src="{{ url_for('static', filename='moscow.jpg') }}" alt="Picture of Moscow">
            <h1>Current Time in Moscow:</h1>
            <p>{{ moscow_time }}</p>
        </div>
    </body>
    <link rel="icon" type="image/x-icon" href="{{ url_for('static', filename='favicon.ico') }}">
    </html>
    """

    return render_template_string(html_template, moscow_time=moscow_time)

if __name__ == '__main__':
    app.run(debug=True)
