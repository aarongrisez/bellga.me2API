from functools import lru_cache
import logging
from typing import Union
from fastapi import WebSocket
from api.models.game import Game
from aiocache import cached
from .connection import WebSocketConnectionManager


logger = logging.getLogger("api")

Message = Game


class MessageManager:

    def __init__(self):
        self.generator = self.get_message_generator()
        self.connection_manager = get_websocket_connection_manager()

    async def get_message_generator(self):
        while True:
            message = yield
            await self._notify(message)
    
    async def push(self, msg: Message):
        await self.generator.asend(msg)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connection_manager.add_connection(websocket)

    async def remove(self, websocket: WebSocket):
        await self.connection_manager.remove_connection(websocket)

    async def send(self, websocket: WebSocket, message: Message):
        await websocket.send_json(message.json())

    async def _notify(self, message: Message):
        await self.connection_manager.apply_to_connections(
            lambda ws: self.send(ws, message)
        )

@lru_cache()
def get_websocket_connection_manager():
    return WebSocketConnectionManager()

@cached()
async def get_message_manager():
    m = MessageManager()
    await m.generator.asend(None)
    return m