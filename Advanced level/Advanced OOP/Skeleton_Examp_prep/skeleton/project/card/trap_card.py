from project.card.card import Card

class TrapCard(Card):

    def __init__(self, name):
        super().__init__(name, damage_point=120, health_points=5)
