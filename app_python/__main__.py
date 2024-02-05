"""HTTP server that returns current MSK time."""
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import pytz


class HTTPTimeHandler(BaseHTTPRequestHandler):
    """Handles GET requests."""

    def do_GET(self):  # pylint: disable=C0103
        """Returns current time in the 'Europe/Moscow'
        timezone with 'text/plain' content type."""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        timezone = pytz.timezone("Europe/Moscow")
        self.wfile.write(str(datetime.now(timezone)).encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    """Starts HTTP server listening on all interfaces on port 8080."""
    server_address = ("", 8080)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    run(handler_class=HTTPTimeHandler)
