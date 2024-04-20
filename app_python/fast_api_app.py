from fastapi import FastAPI, Request

from api import router as api_router
from api.v1.visits.schemas import VisitResponse
from api.v1.visits.crud import get_visits as get_vis, set_visits
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
app.include_router(api_router, prefix="/api")

Instrumentator().instrument(app).expose(app)


@app.middleware('http')
async def catch_visits(request: Request, call_next):
    visits = get_vis() + 1
    set_visits(visits)
    response = await call_next(request)
    return response


@app.get('/visits', response_model=VisitResponse)
def get_visits():
    return VisitResponse(visits=get_vis())
