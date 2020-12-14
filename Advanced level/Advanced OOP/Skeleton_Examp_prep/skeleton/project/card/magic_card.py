from project.card.card import Card


class MagicCard(Card):

    def __init__(self, name):
        super().__init__(name, damage_point=5, health_points=80)
