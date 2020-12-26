from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    auth0_id: str
    username: str
    disabled: Optional[bool] = None