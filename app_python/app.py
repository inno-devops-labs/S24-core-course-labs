from flask import Flask, render_template
from datetime import datetime
import pytz
from prometheus_client import generate_latest

# Create a non-root user if it doesn't exist
# subprocess.call(['adduser', '-D', 'myuser'])
# os.setuid(1000)  # Switch to non-root user

app = Flask(__name__)

@app.route('/')
def index():
    moscow_tz = pytz.timezone('Europe/Moscow')
    moscow_time = datetime.now(moscow_tz).strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', time=moscow_time)

@app.route('/metrics')
def metrics():
    return generate_latest()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
