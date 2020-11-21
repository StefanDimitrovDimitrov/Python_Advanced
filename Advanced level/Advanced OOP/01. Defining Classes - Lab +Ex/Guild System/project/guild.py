from typing import List


class Guild:

    name: str
    list_player: list
    player: List[Player]

    def __init__(self,name, list_players):
        self.name = name
        self.list_players = list_players

    def assign_player (self, player: Player):
        pass


    def kick_player(self, player_name: String):
        pass


    def guild_info():
        pass