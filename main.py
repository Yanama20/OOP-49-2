#Инкапсуляция -
#Абстракция - отделение методов родительского класса от дочерних.

from abc import ABC, abstractmethod

import random

class Hero(ABC):
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self._luck= random.randint(0, 100)
        self.__crit_dmg = random.randint(0, 100)
        self.__random_action = random.randint(1, 3)

    def greeting(self):
        return print(f"Hello {self.name}!\nМой уровень: {self.lvl}.")

    def status(self):
        return print(f'Name: {self.name}\n'
                f'HP: {self.hp}\n'
                f'Level: {self.lvl}\n')

    def attack(self):
        if self.__crit_dmg <= 30:
            return print(f'{self.name} нанёс критический удар')
        else:
            return print(f'{self.name} нанёс базовый удар')

    def defence(self):
        if self._luck <= 20:
            return print(f'{self.name} парировал атаку')
        else:
            return print(f'{self.name} парирование не удалось')

    def __heal_hp(self):
        return random.randint(1, self.hp)

    def rest(self):
        self.hp += self.__heal_hp()
        return print(f'{self.name} полечился на {self.__heal_hp()}.')

    @abstractmethod
    def unique_attack(self):
        pass

    @abstractmethod
    def unique_scream(self):
        pass

# hero = Hero('Andersen', 3000, 40)
# hero.attack()
# hero.defence()
# hero.rest()