from packages.core.entity import Entity

class Business(Entity):
    def __init__(self, name, owner_id):
        super().__init__(name, "business")
        self.owner_id = owner_id
        self.employees = []
        self.inventory = []
        self.balance = 0

    def hire(self, employee_id):
        self.employees.append(employee_id)
