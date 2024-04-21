from datetime import datetime
from zoneinfo import ZoneInfo

from aiohttp import web
from aiohttp_openmetrics import metrics, metrics_middleware

import os


def get_current_time() -> datetime:
    return datetime.now(ZoneInfo("Europe/Moscow"))


VISITS_FILE = "./data/visits"


def sane_opener(name: str, flags: int):
    return os.open(name, flags | os.O_CREAT)


def increment_visits():
    with open(VISITS_FILE, "r+", opener=sane_opener) as f:
        try:
            counter = int(f.read())
        except ValueError:
            counter = 0

        f.seek(0)
        f.write(str(counter + 1))


def get_visits():
    try:
        with open(VISITS_FILE, "r") as f:
            return int(f.read())
    except (ValueError, FileNotFoundError):
        return 0


async def handle(_request: web.Request) -> web.StreamResponse:
    print("handling a request")
    increment_visits()

    current_time = get_current_time()
    response = current_time.isoformat()
    return web.Response(text=response)


async def visits(_request: web.Request) -> web.StreamResponse:
    counter = get_visits()
    return web.Response(text=str(counter))


app = web.Application()
app.add_routes(
    [
        web.get("/", handle),
        web.get("/metrics", metrics),
        web.get("/visits", visits),
    ]
)
app.middlewares.append(metrics_middleware)

if __name__ == "__main__":
    web.run_app(app)
