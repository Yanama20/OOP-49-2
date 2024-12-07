from main import Hero
import main

test = main.Hero

class ShieldHero(Hero):

    def __init__(self, name, hp, lvl, aura=0):
        super().__init__()
        self.aura = aura

    def defence(self):
        if self._luck <= 20:
            return print(f'{self.name} парировал атаку')
        else:
            self.aura += 50
            return print(f'{self.name} парирование не удалось.\n'
                         f'Получено 50 ауры')

    def ultimate(self):
        if self.aura >= 10:
            self.aura -= 10
            return print(f'{self.name} использовал ультимативную способность')
        else:
            return print(f'{self.name} не хватает ауры')

    def battle_scream(self):
        if self.aura >= 1:
            return print("ОРАААА")

naofumi = ShieldHero('Naofumi', 100, 1)
naofumi.attack()
naofumi.defence()