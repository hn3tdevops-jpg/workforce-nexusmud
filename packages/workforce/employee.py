from packages.core.entity import Entity

class Employee(Entity):
    def __init__(self, name, user_id):
        super().__init__(name, "employee")
        self.user_id = user_id
        self.roles = []
