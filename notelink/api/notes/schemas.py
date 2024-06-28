from datetime import datetime

from pydantic import BaseModel


class NoteBaseSchema(BaseModel):
    title: str
    text: str
    expire: datetime


class NoteSchema(NoteBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class NoteCreateSchema(NoteBaseSchema):
    pass
