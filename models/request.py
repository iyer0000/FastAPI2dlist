from pydantic import BaseModel,constr,conlist
from typing import Deque, List, Optional, Tuple


class RequestModel(BaseModel):
    batchid: constr(min_length=6)
    payload:Optional[List[List[int]]] = None
