from pydantic import BaseModel, Field


class MeetingCreate(BaseModel):
    title: str = Field(min_length=3)
    date: str
    owner: str = Field(min_length=2)


class MeetingRead(MeetingCreate):
    id: str
