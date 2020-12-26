from pydantic import BaseModel
from typing import List
from api.models.user import User

class Room(BaseModel):
    name: str
    game: str
    players: List[User]
    maxPlayers: int