from flask import Flask
import ntplib
from time import ctime
from datetime import datetime, timezone
from dateutil import tz

app = Flask(__name__)
ntp_client = ntplib.NTPClient()

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
    return template % moscow_time.strftime("%d/%m/%Y, %H:%M:%S")

