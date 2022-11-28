# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# треугольник
# length = 150
# point = sd.get_point(100, 30)
#
# v1 = sd.get_vector(start_point=point, angle=0, length=150, width=2)
# v1.draw()
# v2 = sd.get_vector(start_point=v1.end_point, angle=120, length=150, width=2)
# v2.draw()
# v3 = sd.get_vector(start_point=v2.end_point, angle=240, length=150, width=2)
# v3.draw()
#
# # квадрат
# point_1 = sd.get_point(300, 10)
# p1 = sd.get_vector(start_point=point_1, angle=0, length=100, width=2)
# p1.draw()
#
# p2 = sd.get_vector(start_point=p1.end_point, angle=90, length=100, width=2)
# p2.draw()
#
# p3 = sd.get_vector(start_point=p2.end_point, angle=+180, length=100, width=2)
# p3.draw()
#
# p4 = sd.get_vector(start_point=p3.end_point, angle=-90, length=100, width=2)
# p4.draw()
#
# # пятиугольник
# point_2 = sd.get_point(100, 200)
# f1 = sd.get_vector(start_point=point_2, angle=0, length=100, width=2)
# f1.draw()
#
# f2 = sd.get_vector(start_point=f1.end_point, angle=70, length=100, width=2)
# f2.draw()
#
# f3 = sd.get_vector(start_point=f2.end_point, angle=140, length=100, width=2)
# f3.draw()
#
# f4 = sd.get_vector(start_point=f3.end_point, angle=215, length=100, width=2)
# f4.draw()
#
# f5 = sd.get_vector(start_point=f4.end_point, angle=285, length=100, width=2)
# f5.draw()
#
# point_3 = sd.get_point(400, 200)
# ff1 = sd.get_vector(start_point=point_3, angle=60, length=100, width=2)
# ff1.draw()
#
# ff2 = sd.get_vector(start_point=ff1.end_point, angle=120, length=100, width=2)
# ff2.draw()
#
# ff3 = sd.get_vector(start_point=ff2.end_point, angle=180, length=100, width=2)
# ff3.draw()
#
# ff4 = sd.get_vector(start_point=ff3.end_point, angle=240, length=100, width=2)
# ff4.draw()
#
# ff5 = sd.get_vector(start_point=ff4.end_point, angle=300, length=100, width=2)
# ff5.draw()
#
# ff6 = sd.get_vector(start_point=ff5.end_point, angle=360, length=100, width=2)
# ff6.draw()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?




# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point

def polygon(point, heads, length):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_RED, width=2)
        point = end_point


start_point = [(100,100,150,3), (350, 100, 150, 4), (100, 350, 100, 5), (350,350,100,6) ]


for _ in start_point:
    point_start = sd.get_point(_[0], _[1])
    length_start = _[2]
    heads_start = _[3]
    polygon(point_start, heads_start,length_start)
sd.pause()
