from main import Hero

class Jester(Hero):
    def __init__(self, name, hp, lvl):
         super().__init__(name, hp, lvl)

    def unique_attack(self):
        return f'{self.name} использовал уникальный навык'

    def unique_scream(self):
        return f'{self.name} издал боевой клич'

    def action(self):
        if self._Hero__random_action == 1:
            return print(Hero.attack(self))
        elif self._Hero__random_action == 2:
            return print(Hero.defence(self))
        elif self._Hero__random_action == 3:
            return print(Hero.rest(self))

joker = Jester('Joker', 800, 15)
print(joker.action())