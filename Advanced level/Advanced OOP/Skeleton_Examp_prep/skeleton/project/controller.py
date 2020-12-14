class Controller:

    def __init(self, player_repository, card_repository):
        self.player_repository = player_repository
        self.card_repository = card_repository

    def add_player(self, type: str, username: str):
        pass

    def add_card(self, type: str, name: str):
        pass

    def add_player_card(self, username: str, card_name: str):
        pass

    def fight(self, attack_name: str, enemy_name: str):
        pass

    def report(self):
        pass
