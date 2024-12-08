#Инкапсуляция -
#Абстракция - отделение методов родительского класса от дочерних.

from abc import ABC, abstractmethod

import random

class Hero(ABC):
    def __init__(self, name='Geralt', hp=100, lvl=1):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        #Защищённый атрибут
        self._luck= random.randint(0, 100)
        #Приватный атрибут
        self.__crit_dmg = random.randint(0, 100)

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
    def ultimate(self):
        pass

    @abstractmethod
    def battle_scream(self):
        pass

# hero = Hero('Andersen', 3000, 40)
# hero.attack()
# hero.defence()
# hero.rest()

# class ShieldHero(Hero):
#
#     def __init__(self, name, hp, lvl, aura=0):
#         super().__init__()
#         self.aura = aura
#
#     def defence(self):
#         if self._luck <= 20:
#             return print(f'{self.name} парировал атаку')
#         else:
#             self.aura += 50
#             return print(f'{self.name} парирование не удалось.\n'
#                          f'Получено 50 ауры')
#
#     def ultimate(self):
#         if self.aura >= 10:
#             self.aura -= 10
#             return print(f'{self.name} использовал ультимативную способность')
#         else:
#             return print(f'{self.name} не хватает ауры')
#
#     def battle_scream(self):
#         if self.aura >= 1:
#             return print("ОРАААА")
#
# naofumi = ShieldHero('Naofumi', 100, 1)
# naofumi.attack()
# naofumi.defence()

# Множественное наследование Решается с помощью MRO(

class Animal:
    def make_sound(self):
        return "Звук"

class Flyable:
    def move(self):
        return 'Летит'

class Swimable:
    def move(self):
        return 'Плывёт'

class Duck(Animal, Flyable, Swimable):
    def make_sound(self):
        return 'Кря-Кря!'

# donald = Duck()
# print(donald.make_sound())
# print(donald.move())

# Алмазная проблема

class A:
    def sound(self):
        print("A")

class B(A):
    def sound(self):
        super().sound()
        print('B')

class C(A):
    def sound(self):
        super().sound()
        print('C')

class D(B, C):
    def sound(self):
        super().sound()
        print('D')

# d = D()
# d.sound()