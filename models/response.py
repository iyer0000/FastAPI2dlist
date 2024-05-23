from pydantic import BaseModel,constr
from datetime import date, datetime
from typing import List, Optional


class ResponseModel(BaseModel):
    batchid: constr(max_length=6)
    response:Optional[List[int]]
    status: constr(max_length=8)
    started_at:  datetime = None
    completed_at: datetime = None
