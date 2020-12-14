from abc import ABC

from project.player.player import Player


class PlayerRepository(ABC):

    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        player_with_current_name = next([p for p in self.players if p.name == player.username])
        if player_with_current_name:
            raise ValueError(f"Player {player.username} already exists!")

        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == '':
            raise ValueError("Player cannot be an empty string!")

        player_with_current_name = next([p for p in self.players if p.name == player])

        if player_with_current_name:
            self.players.remove(player_with_current_name)
            self.count -= 1

    def find(self, username: str):
        player_with_current_name = next([p for p in self.players if p.name == username])
        return player_with_current_name
