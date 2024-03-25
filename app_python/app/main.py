from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
from prometheus_fastapi_instrumentator import Instrumentator
import zoneinfo

app = FastAPI()


# This function returns the HTML content for the root page
async def get_root_page() -> str:
    moscow_time = datetime.now(zoneinfo.ZoneInfo(
        "Europe/Moscow")).strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
    <html>
        <head>
            <title>Moscow Time App</title>
            <style>
                .moscow-time {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    flex-direction: column;
                    font-family: Arial, sans-serif;
                }}
            </style>
        </head>
        <body>
            <div class="moscow-time">
                <h1>Current Moscow Time</h1>
                <h2>{moscow_time}</h2>
            </div>
        </body>
    </html>
    """

    return html_content


@app.get("/")
async def root():
    html_content = await get_root_page()
    return HTMLResponse(content=html_content, status_code=200)


# Run using Instrumentator to add metrics
if __name__ == "__main__":
    Instrumentator().instrument(app).expose(app)
