class EntityRegistry:
    def __init__(self):
        self.entities = {}

    def register(self, entity):
        self.entities[entity.entity_id] = entity

    def get(self, entity_id):
        return self.entities.get(entity_id)
