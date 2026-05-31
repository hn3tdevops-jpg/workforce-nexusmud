from packages.core.entity import Entity

class Organization(Entity):
    def __init__(self, name):
        super().__init__(name, "organization")
        self.members = []
