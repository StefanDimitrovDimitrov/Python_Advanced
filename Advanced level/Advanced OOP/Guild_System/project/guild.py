from project.player import Player


class Guild:
    list_of_players = []

    def __init__(self, name):
        self.name = name
        self.list_of_players = []

    def assign_player(self, player: Player):

        if player.guild == "Unaffiliated":
            player.guild = self.name
            self.list_of_players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        if player.guild != self.name:
            return f"Player {player.name} is in another guild."

        return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name: str):
        players_with_given_name = [p for p in self.list_of_players if p.name == player_name]

        if not players_with_given_name:
            return f"Player {player_name} is not in the guild."

        self.list_of_players.remove(players_with_given_name[0])
        players_with_given_name[0].guild = "Unaffiliated"

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}",
                  '\n'.join([p.player_info() for p in self.list_of_players])]
        # result = ''.join([p.player_info() for p in self.list_of_players])
        return "\n".join(result)
