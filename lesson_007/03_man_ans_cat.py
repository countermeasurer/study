# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытность {}'.format(self.name, self.fullness)

    def go_into_the_home(self, house):
        self.house = house
        self.fullness -= 10
        print('{} подобрал Барт'.format(self.name))

    def eat(self):
        if self.house.cfood >= 10:
            print('{} поел, корма осталось {}'.format(self.name, self.house.cfood))
            self.fullness += 20
            self.house.cfood -= 10
        else:
            print('{} не смог поесть, в доме не осталось корма'.format(self.name, self.house.cfood))


    def sleep(self):
        print('{} спал весь день'.format(self.name))
        self.fullness -= 10


    def demage(self):
        print('{} начал драть обои'.format(self.name))
        self.fullness -= 10
        self.house.trash += 5


    def act(self):
        if self.fullness <= 0:
            print('{} умер от голода'.format(self.name))
            return
        dice = randint(1,3)
        if self.fullness < 20:
            self.eat()
        elif self.house.trash <= 50:
            self.demage()
        else:
            self.sleep()

class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Парень - {}, сытность {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'. format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} не смог поесть, нет еды('.format(self.name))


    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 20



    def coding(self):
        print('{} кодил весь день'.format(self.name))
        self.fullness -= 20


    def shopping(self):
        if self.house.money >= 100:
            print('{} сходил в магазин за продуктами'.format(self.name))
            self.house.money -= 100
            self.fullness -= 15
            self.house.food += 50
            self.house.cfood += 50
        else:
            print('{} деньги кончились'.format(self.name))


    def go_into_the_home(self, house):
        self.house = house
        self.fullness -= 10
        print('{} Въехал в дом'.format(self.name))

    def clear(self):
        if self.house.trash >= 100:
            print('{} прибрался дома'.format(self.name))
            self.house.trash -= 100
        else:
            print('{} Не смог убраться дома, уровень грязи остался {}'.format(self.name, self.house.trash))


    def act(self):
        if self.fullness <= 0:
            print('{} умер от голода'.format(self.name))
            return
        dice = randint(1, 6)
        if self.house.food and self.house.cfood <= 50:
            self.shopping()
        elif self.fullness < 10:
            self.eat()
        elif self.house.money < 150:
            self.work()
        elif self.house.trash >= 55:
            self.clear()
        elif dice == 1:
            self.work()
        else:
            self.coding()

class House:
    def __init__(self):
        self.food = 50
        self.cfood = 50
        self.money = 0
        self.trash = 0

    def __str__(self):
        return 'В дома осталось {}, дошираков и кошачьего корма {}, ' \
               'денег осталось {}, уровень мусора = {}'.format(self.food, self.cfood, self.money, self.trash)


citizens = [
    Man(name='Барт'),
    Cat(name='Маффин')
]

my_sweet_home = House()
for citizen in citizens:
    citizen.go_into_the_home(house=my_sweet_home)

for day in range(1, 366):
    print('============== day {} =============='.format(day))
    for citizen in citizens:
        citizen.act()
    print('--- finish day ---')
    for citizen in citizens:
        print(citizens)
    print(my_sweet_home)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
