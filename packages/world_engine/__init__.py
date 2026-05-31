
class Room:
    def __init__(self, room_id, name, description):
        self.room_id = room_id
        self.name = name
        self.description = description
        self.players = []

    def enter(self, player_name):
        self.players.append(player_name)
        return f"{player_name} entered {self.name}"

    def leave(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            return f"{player_name} left {self.name}"
