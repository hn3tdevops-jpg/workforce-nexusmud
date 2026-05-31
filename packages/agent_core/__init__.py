
class Agent:
    def __init__(self, name, role, personality):
        self.name = name
        self.role = role
        self.personality = personality

    def speak(self, message):
        return f"{self.name} ({self.role}): {message}"
