"""
Python Web Application
"""
from datetime import datetime, timezone
from textwrap import dedent
from zoneinfo import ZoneInfo

from ntplib import NTPClient
from sanic import Sanic
from sanic_ext import render

from app_python.app.config import AppConfig

app = Sanic("MoscowTime", config=AppConfig())


@app.before_server_start
async def setup_ntp(appl):
    """
    Setup NTP client before main server
    """
    appl.ctx.ntp = NTPClient()


@app.get("/")
async def index_handle(request):
    """
    Index handler

    Requests current time from Google NTP server and returns a template with it
    """
    template = dedent(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Moscow Time</title>
        </head>
        <body>
            <h1>Hello, Moscow!!!!</h1>
            <h2>{{ moscow_time }}</h2>
        </body>
        </html>
        """
    )

    ntp_client = app.ctx.ntp
    response = ntp_client.request(
        request.app.config.NTP_SERVER,
        version=request.app.config.NTP_VERSION)
    utc_time = datetime.fromtimestamp(response.tx_time, tz=timezone.utc)
    moscow_time = datetime.astimezone(utc_time, tz=ZoneInfo("Europe/Moscow"))

    return await render(
        template_source=template,
        context={'moscow_time': moscow_time.ctime()},
        app=app,
    )


def get_app():
    return app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
