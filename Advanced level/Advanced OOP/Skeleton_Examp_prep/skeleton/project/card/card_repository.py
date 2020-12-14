from project.card.card import Card


class CardRepository:

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        card_with_current_name = next([c for c in self.cards if c.name == card.name])

        if card_with_current_name:
            raise ValueError(f"card {card.name} already exists!")

        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("card cannot be an empty string!")

        card_with_current_name = next([c for c in self.cards if c.name == card])

        if card_with_current_name:
            self.cards.remove(card_with_current_name)
            self.count -= 1

    def find(self, name: str):
        card_with_current_name = next([c for c in self.cards if c.name == name])
        return card_with_current_name

