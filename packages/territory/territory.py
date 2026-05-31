from packages.core.entity import Entity

class Territory(Entity):
    def __init__(self, name):
        super().__init__(name, "territory")
        self.owner_id = None
        self.tax_rate = 0
        self.structures = []
        self.reputation_bonus = 0
