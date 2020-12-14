from project.player.player import Player


class Battle_field:

    def __init__(self):
        pass

    def check_if_it_is_begginer(self, player):
        if type(player) == "beginner":
            player.health += 40
            player.card_repository.cards = [card.demage_point + 30 for card in player.card_repository.cards]

    def get_bonus(self, player):
        bonus_points = sum([c.health_points for c in player.card_repository.cards])
        player.health += bonus_points

    def check_if_player_is_dead(self, player):
        if player.is_dead:
            raise ValueError("Player is dead!")

    def attack(self, player_attacker, player_enemy, card_index):
        player_enemy.health -= player_attacker.card_repository.cards[card_index].damage_point
        if player_enemy.health <= 0:
            player_enemy.is_dead = True

    def fight(self, attacker: Player, enemy: Player):

        self.check_if_it_is_begginer(attacker)
        self.check_if_it_is_begginer(enemy)
        self.get_bonus(attacker)
        self.get_bonus(enemy)

        next_card = -1
        while True:
            next_card += 1
            self.attack(attacker, enemy, next_card)
            self.check_if_player_is_dead(enemy)
            self.attack(enemy, attacker, next_card)
            self.check_if_player_is_dead(attacker)
