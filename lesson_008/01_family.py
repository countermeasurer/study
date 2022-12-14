# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.produkti = 0
        self.mess = 0

    def __str__(self):
        return '{} - Денег в тумбочке, {} - еды в холодильнике, {} - продуктов дома'.format(self.money, self.food,
                                                                                            self.produkti)



class Human:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        if self.fullness > 100:
            self.fullness = 100
        if self.happiness > 100:
            self.happiness = 100
        return '{} , сытность - {} , счастье - {}'.format(self.name,self.fullness,self.happiness)

    def eat(self, need_food):

        if self.house.food >= need_food:
            self.house.food -= need_food
            self.fullness += need_food
            print('{} ест'.format(self.name))

    def carres(self):
        pass


class Husband(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.need_food = 30

    def act(self):
        i = randint(1, 3)
        if self.house.mess >= 100:
            self.happiness -= 10
        if self.happiness <= 0:
            print('{} умер от горя'.format(self.name))
        if self.fullness <= 0:
            print('{} умер от голода'.format(self.name))
        elif self.fullness <= 10:
            self.eat()
        elif self.house.money <= 150:
            self.work()
        elif i == 1:
            self.work()
        elif i == 2:
            self.gaming()
        else:
            self.gaming()

    def eat(self):

        super().eat(self.need_food)

    def work(self):
        self.house.money += 150
        self.fullness -= 10
        print('{} сходил на работу'.format(self.name))

    def gaming(self):
        self.happiness += 10
        self.fullness -= 10
        print('{} играл в WOT весь день'.format(self.name))


class Wife(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.need_food = 30


    def act(self):
        i = randint(1, 5)
        if self.house.mess >= 100:
            self.happiness -= 10
        if self.happiness <= 0:
            cprint('{} умерла от горя'.format(self.name), color='red')
        if self.fullness <= 0:
            cprint('{} умерла от голода'.format(self.name), color='red')
        elif self.fullness <= 10:
            self.eat()
        elif self.house.food <= 30:
            self.working()
        elif self.house.produkti <= 30:
            self.shopping()
        elif self.house.mess >= 100:
            self.clean_house()
        elif i == 1:
            self.buy_fur_coat()
        elif i == 2:
            self.clean_house()
        else:
            self.shopping()


    def eat(self):
        super().eat(self.need_food)

    def shopping(self):
        if self.house.money >= 50:
            self.house.money -= 50
            self.house.produkti += 50
            self.happiness += 10
            self.fullness -= 10
            print('{} сходила в магазин за продуктами'.format(self.name))

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.house.money -= 350
            self.happiness += 90
            self.fullness -= 10
            print('{} купила шубу'.format(self.name))

    def clean_house(self):
        if self.house.mess <= 100:
            self.house.mess = 0
            self.fullness -= 10
            print('{} убралась в доме'.format(self.name))
        else:
            self.house.mess -= 100
            self.happiness -= 10
            print('{} убралась в доме'.format(self.name))


    def working(self):
        if self.house.food >= 10:
            print('{} готовит еду'.format(self.name))
            self.house.produkti -= 10
            self.house.food += 10
            self.fullness -= 10
        else:
            print('{} не смогла приготовить еду. Продуктов нет'.format(self.name))


home = House()
serge = Husband(name='Сережа', house=home)
masha = Wife(name='Маша', house=home)

for day in range(21):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')


# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа',house=home)
# masha = Wife(name='Маша',house=home)
# # kolya = Child(name='Коля')
# # murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     # kolya.act()
#     # murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     # cprint(kolya, color='cyan')
#     # cprint(murzik, color='cyan')
#
# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
