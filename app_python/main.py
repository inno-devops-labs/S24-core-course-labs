from flask import Flask
import fcntl
import ntplib
import os
from time import ctime
from datetime import datetime, timezone
from dateutil import tz

app = Flask(__name__)
ntp_client = ntplib.NTPClient()

@app.route("/visits")
def get_visits_count():
    with open("/app_python/persistent/visits") as file:
        return file.read()

@app.route("/")
def get_moscow_time():
    template = """
        <style>body {
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            font-size: 350%%;
        }</style>
        <script>
            setTimeout(function(){
                window.location.reload(1);
            }, 1000);
        </script>
        <h1>%s</h1>
    """
    
    try:
        ntp_response = ntp_client.request('ru.pool.ntp.org', version=3)
        time = datetime.utcfromtimestamp(ntp_response.tx_time)
    except:
        time = datetime.now(timezone.utc)

    moscow_time = time.replace(tzinfo=tz.tzutc()).astimezone(tz.gettz("Europe/Moscow"))
    
    try:
        with open("/app_python/persistent/visits", "r+") as file:
            fcntl.flock(file, fcntl.LOCK_EX)
            current_cnt = int(file.read())
            try:
                file.truncate(0)
                file.seek(0)
                file.write(str(current_cnt + 1))
                file.flush()
                os.fsync(file.fileno())
            finally:
                fcntl.flock(file, fcntl.LOCK_UN)
    except:
        with open("/app_python/persistent/visits", "w") as file:
            file.write("1")

    return template % moscow_time.strftime("%d/%m/%Y, %H:%M:%S")


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5000)
