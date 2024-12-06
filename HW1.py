class Person:
    # 1-ое задание
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def introduce(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}')
    # 2-ое задание
    def is_adult(self):
        self.age = int(self.age)
        if self.age >= 18:
            return True
        else:
            return False
    # 3-е задание
    def __str__(self):
        return f'Имя: {self.name}, Возраст: {self.age}, Город: {self.city}'

print('1-ое задание')
person_Aman = Person('Аман', '20', 'Бишкек')
person_Aman.introduce()

print('2-ое задание')
person_Danil = Person('Улан', '16', 'Бишкек')
person_Aidai = Person('Айдай', '24', 'Нью-Йорк')
person_Artur = Person('Артур', '22', 'Париж')
print(person_Danil.is_adult())
print(person_Aidai.is_adult())
print(person_Artur.is_adult())

print('3-е задание')
person_Vasya = Person('Вася', '18', 'Москва')
print(person_Vasya)