# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.background_color = (0, 0, 0)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
start_point = (50, 50)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

"""start_x, start_y = 50, 50
end_x, end_y = 350, 450
sd.resolution = (500, 500)

for current_color in rainbow_colors:
    start_point = sd.get_point(start_x, start_y)
    end_point = sd.get_point(end_x, end_y)
    sd.line(start_point, end_point, color=current_color, width= 4)
    start_x += 5
    end_x += 5"""

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код
start_x, start_y = 250, 0
sd.resolution = (500, 500)
for current_color in rainbow_colors:
    center_position = sd.get_point(start_x, start_y)
    sd.circle(center_position=center_position, radius=400, color=current_color, width=35)
    start_y -=20

sd.pause()
