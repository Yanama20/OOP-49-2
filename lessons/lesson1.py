#ООП - обектно ориентированное программирование, Git
#Наследование -
#Инкапсуляция -
#Абстракция -
#Полиморфизм - изменение/переназначение существующих методов

#class - сущность

class Car:
    #Конструктор
    def __init__(self, this_color, this_model, this_year):
        #Атрибуты класса/Field
        self.model = this_model
        self.year = this_year
        self.color = this_color
    #Метод класса
    def signal(self):
        return print(f'{self.model} BMW просигналила')
    def max_speed(self):
        if self.model == 'BMW':
            print('Супер быстрая машина')
        else:
            print('Просто быстрая машина')
    def __str__(self):
        return f'Model: {self.model}, Color: {self.color}, Year: {self.year}'

#Экзэмпляр класса
car_bmw = Car('blue', 'BMW', '2019')
car_honda = Car('black', 'Honda Fit', '2010')

# car_bmw.max_speed()
# car_honda.max_speed()
print(car_bmw)

# 1) git config --global user.name "Your Name"
# 2) git config --global user.email "your@email"
#
# Команды которые пишутся один раз на проект
# 1) git init
# 2) git remote add origin ваша ссылка
#
# Команды которые пишутся часто
# 1) git status ---- показывает статус проекта
# 2) git add . ---- добавляет изменения в буфер
# 3) git commit -m "комментарий" ---- создает коммит ( Сохраняет изменения )
# 4) git branch ---- показывает ветки атак же показыввает текущую ветку
# 5) git push origin master ---- отправляет изменения на github