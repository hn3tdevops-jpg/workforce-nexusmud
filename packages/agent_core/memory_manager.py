class MemoryManager:
    def __init__(self):
        self.memories = []

    def remember(self, memory):
        self.memories.append(memory)

    def for_entity(self, entity_id):
        return [m for m in self.memories if m.target_id == entity_id]
