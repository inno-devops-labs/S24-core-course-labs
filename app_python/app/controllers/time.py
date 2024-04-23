import os
from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.time import get_time_in_msk

router = APIRouter(
    prefix="/time",
    tags=["time"])


class CurrentTimeResponse(BaseModel):
    current_time: datetime


@router.get(
    path="/msk",
    responses={200: {"description": "Success"}})
def get_current_time_in_msk_timezone(
        current_time_in_msk: datetime = Depends(get_time_in_msk)) \
        -> CurrentTimeResponse:
    try:
        with open("data/visits", 'r') as file:
            current_visits = int(file.read())
    except FileNotFoundError:
        current_visits = 0

    os.makedirs(os.path.dirname('data/'), exist_ok=True)
    with open("data/visits", "w+") as file:

        file.write(str(current_visits + 1))
    return CurrentTimeResponse(current_time=current_time_in_msk)
