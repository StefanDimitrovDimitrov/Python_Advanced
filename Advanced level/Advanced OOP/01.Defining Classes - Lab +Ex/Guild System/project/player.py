class Player:
    name: str
    hp: int
    mp: int

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

        self.skills = {}
        guild = "Unaffiliated"

    def skill(self, skill_name, mana_cost):
        pass

    def player_info(self):
        pass