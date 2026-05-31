class AI_NPC:
    def __init__(self, npc_id: str, name: str, role: str, room_id: str):
        self.npc_id = npc_id
        self.name = name
        self.role = role
        self.room_id = room_id
        
    def respond_to(self, player_id: str, message: str) -> str:
        if "quest" in message.lower():
            from packages.world_engine.engine import SessionLocal, Quest
            db = SessionLocal()
            existing = db.query(Quest).filter(Quest.player_id == player_id, Quest.title == f"Help {self.name}").first()
            if not existing:
                q = Quest(
                    player_id=player_id, 
                    title=f"Help {self.name}", 
                    description=f"Find the lost artifact for {self.name} the {self.role}."
                )
                db.add(q)
                db.commit()
                db.close()
                return f"{self.name} gives you a quest: Help {self.name}!"
            db.close()
            return f"{self.name} says: 'You already have my quest!'"
            
        return f"{self.name} smiles at {player_id}. 'I am but a humble {self.role}. I hear you say: {message}'"

class NPCManager:
    def __init__(self):
        self.npcs = {
            "guard_1": AI_NPC("guard_1", "Captain Valerius", "Guard", "north_gate"),
            "merchant_1": AI_NPC("merchant_1", "Elara", "Merchant", "town_square")
        }

    def get_npcs_in_room(self, room_id: str):
        return [npc for npc in self.npcs.values() if npc.room_id == room_id]

    def handle_interaction(self, room_id: str, player_id: str, message: str):
        # A real implementation might route to the specific NPC being talked to
        npcs_here = self.get_npcs_in_room(room_id)
        responses = []
        for npc in npcs_here:
            responses.append(npc.respond_to(player_id, message))
        return responses
