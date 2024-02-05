from app.api import di
from fastapi import APIRouter, Depends, responses

router = APIRouter()


@router.get('/', tags=["time"], response_class=responses.HTMLResponse)
async def show_time(time_manager = Depends(di.time_manager)):  # noqa: E251
    return """
    <html>
        <head>
            <title>Time</title>
        </head>
        <body>
            <h1>{}</h1>
        </body>
    </html>
    """.format(await time_manager.str_time())
