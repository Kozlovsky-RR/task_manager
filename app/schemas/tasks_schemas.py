from pydantic import BaseModel
from app.database import Status


class STaskAdd(BaseModel):
    name_tsk: str
    description: str
    status: Status
    user_id: int


class STask(STaskAdd):
    id: int


class STaskID(BaseModel):
    ok: bool = True
    task_id: int
