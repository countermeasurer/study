#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = [
 'Father', 'Mother', 'Me', 'Grandmother', 'Uncle'
]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Jacob', 177],
    ['Rihanna', 170],
    ['Travis', 180],
    ['Quavo', 190],
    ['Lil Wyane', 168]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(my_family[0],'height', '-', my_family_height[0][1], 'cm')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
x =  my_family_height[0][1]
y =  my_family_height[1][1]
z =  my_family_height[2][1]
q =  my_family_height[3][1]
e =  my_family_height[4][1]
max = x + y + z + q + e
print('Общий рост моей семьи','-',max,'cm')