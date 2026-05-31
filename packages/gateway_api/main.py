import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
import uvicorn
from typing import Dict, List
import json

from packages.world_engine.engine import WorldEngine

app = FastAPI(title="NexusMUD Gateway API")
world_engine = WorldEngine()

class ConnectionManager:
    def __init__(self):
        # player_id -> WebSocket
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, player_id: str):
        await websocket.accept()
        self.active_connections[player_id] = websocket

    def disconnect(self, player_id: str):
        if player_id in self.active_connections:
            del self.active_connections[player_id]

    async def send_personal_message(self, message: str, player_id: str):
        if player_id in self.active_connections:
            await self.active_connections[player_id].send_text(message)

    async def broadcast(self, message: str, player_ids: List[str]):
        for player_id in player_ids:
            if player_id in self.active_connections:
                await self.active_connections[player_id].send_text(message)

manager = ConnectionManager()

@app.get("/health")
def health():
    return {"status": "online", "service": "NexusMUD Gateway"}

@app.websocket("/ws/{player_id}")
async def websocket_endpoint(websocket: WebSocket, player_id: str):
    await manager.connect(websocket, player_id)
    
    # Enter the world
    welcome_msg, room_players = world_engine.player_connect(player_id)
    await manager.send_personal_message(welcome_msg, player_id)
    # Broadcast to others in the room
    await manager.broadcast(f"{player_id} has entered the realm.", [p for p in room_players if p != player_id])
    
    try:
        while True:
            data = await websocket.receive_text()
            # Parse command
            response, broadcast_msg, target_players = world_engine.process_command(player_id, data)
            
            if response:
                await manager.send_personal_message(response, player_id)
            if broadcast_msg and target_players:
                await manager.broadcast(broadcast_msg, [p for p in target_players if p != player_id])
                
    except WebSocketDisconnect:
        manager.disconnect(player_id)
        room_players = world_engine.player_disconnect(player_id)
        await manager.broadcast(f"{player_id} has left the realm.", room_players)
