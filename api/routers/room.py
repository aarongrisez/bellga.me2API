from fastapi import APIRouter, Request
from api.models.room import Room
from api.models.user import User
from api.config.settings import settings
from api.core.database import client
from api import app
from typing import Any, List
import uuid

router = APIRouter()

@router.get("/rooms/", response_model=List[Room])
def get_rooms():
    rsc = client["dev"]["rooms"]
    rs = list(r for r in rsc.find())
    return rs

@app.managers.auth.require_auth
def handle_create_room(game: str, request: Request):
    rooms_collection = client["dev"]["rooms"]
    users_collection = client["users"]["users"]

    user = User(**users_collection.find_one({
        "auth0_id": request.state.user_info["sub"]
    }))

    room = Room(
        name=f"wet-albatross-{str(uuid.uuid4())[:8]}",
        game=game,
        players=[user.dict()],
        maxPlayers=2
    )
    rooms_collection.insert_one(room.dict())
    return room

@router.post("/rooms/{game}/create", response_model=Room)
def create_room(game: str, request: Request):
    return handle_create_room(game, request=request)

def init(app):
    app.include_router(router)