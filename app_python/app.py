from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__, template_folder= 'template')

@app.route('/')
def index():
    moscow_time = get_moscow_time()
    return render_template('index.html', time=moscow_time)

def get_moscow_time():
    # Call this function to calculate moscow time with the help of datetime library
    utc_now = datetime.utcnow()
    moscow_time = utc_now + timedelta(hours=3)
    return moscow_time.strftime('%H:%M:%S')

if __name__ == '__main__':
    app.run(debug=True)
