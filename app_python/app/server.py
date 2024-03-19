"""
Python Web Application
"""
from datetime import datetime, timezone
from textwrap import dedent
from zoneinfo import ZoneInfo

from ntplib import NTPClient
from sanic import Sanic, response
from sanic_ext import render
import prometheus_client as prometheus

from config import AppConfig

request_counter = prometheus.Counter("sanic_requests_total",
                                     "Track the total number of requests",
                                     ["method", "endpoint"])

request_time = prometheus.Summary("sanic_request_time",
                                  "Track the time",
                                  ["method", "endpoint"])

app = Sanic("MoscowTime", config=AppConfig())


@app.middleware('request')
async def track_requests(request):
    # Increase the value for each request
    # pylint: disable=E1101
    request_counter.labels(method=request.method,
                           endpoint=request.path).inc()


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
    start_time = datetime.now()
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

    end_time = datetime.now()

    request_time.labels(method=request.method, endpoint=request.path).observe(end_time.timestamp() - start_time.timestamp())
    return await render(
        template_source=template,
        context={'moscow_time': moscow_time.ctime()},
        app=app,
    )


@app.get("/metrics")
async def metrics(request):
    output = prometheus.exposition.generate_latest().decode("utf-8")
    content_type = prometheus.exposition.CONTENT_TYPE_LATEST
    return response.text(body=output,
                         content_type=content_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
