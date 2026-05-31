class RelationshipEngine:
    def __init__(self):
        self.relationships = {}

    def modify(self, npc_id, player_id, delta):
        key = (npc_id, player_id)
        self.relationships[key] = self.relationships.get(key, 0) + delta

    def score(self, npc_id, player_id):
        return self.relationships.get((npc_id, player_id), 0)
