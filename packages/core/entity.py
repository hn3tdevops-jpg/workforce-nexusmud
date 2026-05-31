from dataclasses import dataclass, field
from uuid import uuid4

@dataclass
class Entity:
    name: str
    entity_type: str
    entity_id: str = field(default_factory=lambda: str(uuid4()))
    metadata: dict = field(default_factory=dict)

    def serialize(self):
        return {
            "id": self.entity_id,
            "name": self.name,
            "type": self.entity_type,
            "metadata": self.metadata
        }
