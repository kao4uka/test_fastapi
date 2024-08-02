from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Message(BaseModel):
    content: str
    username: Optional[str]
    timestamp: datetime = datetime.utcnow()
