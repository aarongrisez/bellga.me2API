from fastapi import WebSocket
from typing import Any, Callable
import logging


logger = logging.getLogger("api")


class WebSocketConnectionManager:

    def __init__(self):
        self.connections = []
    
    def add_connection(self, connection: WebSocket) -> WebSocket:
        self.connections.append(connection)
        return connection
        
    async def remove_connection(self, connection: WebSocket) -> WebSocket:
        await connection.close(code=1000)
        self.connections.remove(connection)
        return connection
    
    async def apply_to_connections(self, function: Callable[...,Any]) -> None:
        living_connections = []
        while len(self.connections) > 0:
            # Looping like this is necessary in case a disconnection is handled
            # during await websocket.send_text(message)
            websocket = self.connections.pop()
            await function(websocket)
            living_connections.append(websocket)
        self.connections = living_connections