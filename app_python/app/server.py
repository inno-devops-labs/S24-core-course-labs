"""
Python Web Application
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from ntplib import NTPClient
from sanic import Sanic

from config import AppConfig

app = Sanic("MoscowTime", config=AppConfig())


@app.before_server_start
async def setup_ntp(appl):
    """
    Setup NTP client before main server
    """
    appl.ctx.ntp = NTPClient()


@app.get("/")
@app.ext.template("index.html")
async def index_handle(request):
    """
    Index handler

    Requests current time from Google NTP server and returns a template with it
    """
    ntp_client = app.ctx.ntp
    response = ntp_client.request(
        request.app.config.NTP_SERVER,
        version=request.app.config.NTP_VERSION)
    utc_time = datetime.fromtimestamp(response.tx_time, tz=timezone.utc)
    moscow_time = datetime.astimezone(utc_time, tz=ZoneInfo("Europe/Moscow"))

    return {'moscow_time': moscow_time.ctime()}
