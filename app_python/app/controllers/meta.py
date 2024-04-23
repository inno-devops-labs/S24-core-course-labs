from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.time import get_time_in_msk

router = APIRouter(
    prefix="",
    tags=["meta"])


class VisitsResponse(BaseModel):
    visits: int


@router.get(
    path="/visits",
    responses={200: {"description": "Success"}})
def get_current_time_in_msk_timezone() -> VisitsResponse:
    try:
        return VisitsResponse(visits=int(open("visits").read()))
    except:
        return VisitsResponse(visits=0)
