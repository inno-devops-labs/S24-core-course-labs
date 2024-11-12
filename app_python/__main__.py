"""HTTP server that returns current MSK time."""
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
from prometheus_client import Counter, generate_latest
import os
import sys
import pytz


def get_time():
    """Returns current MSK time."""
    timezone = pytz.timezone("Europe/Moscow")
    return datetime.now(timezone)


def inc_counter():
    cnt = get_counter()

    with open("/var/visits/cnt", "w") as fout:
        fout.write(str(cnt + 1))


def get_counter():
    with open("/var/visits/cnt", "r") as fin:
        return int(fin.read())


class HTTPTimeHandler(BaseHTTPRequestHandler):
    """Handles GET requests."""

    def do_GET(self):  # pylint: disable=C0103
        """Returns current time in the 'Europe/Moscow'
        timezone with 'text/plain' content type."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        if self.path == "/metrics":
            self.wfile.write(generate_latest())
        elif self.path == "/var/visits":
            self.wfile.write(f"Visits: {get_counter()}".encode())
        else:
            inc_counter()
            self.wfile.write(str(get_time()).encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """Starts HTTP server listening on all interfaces on port 8080."""
    server_address = ("", 8080)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    if not os.path.exists("/var/visits"):
        os.mkdir("/var/visits")
        # sys.exit(-1111111)
    if not os.path.isfile("/var/visits/cnt"):
        with open("/var/visits/cnt", "w") as fout:
            fout.write("0")

    run(handler_class=HTTPTimeHandler)
