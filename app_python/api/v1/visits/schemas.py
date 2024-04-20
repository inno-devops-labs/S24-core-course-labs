from pydantic import BaseModel, Field


class VisitResponse(BaseModel):
    visits: int = Field(0, ge=0)
