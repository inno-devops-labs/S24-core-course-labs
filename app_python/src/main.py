from datetime import datetime
from zoneinfo import ZoneInfo

from aiohttp import web


def get_current_time() -> datetime:
    return datetime.now(ZoneInfo("Europe/Moscow"))


async def handle(_request: web.Request) -> web.StreamResponse:
    current_time = get_current_time()
    response = current_time.isoformat()
    return web.Response(text=response)


app = web.Application()
app.add_routes([web.get("/", handle)])

if __name__ == "__main__":
    web.run_app(app)
