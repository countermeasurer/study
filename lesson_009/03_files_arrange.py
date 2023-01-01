# -*- coding: utf-8 -*-

import os, time, shutil, zipfile
from abc import ABCMeta, abstractmethod

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class FileSorter:
    def __init__(self, original_name, target_name):
        self.original_name = os.path.normpath(original_name)
        self.target_name = os.path.normpath(target_name)

    def do_it(self):
        for dirpath, dirname, filename in os.walk(self.original_name):
            if filename:
                for file in filename:
                    file_path = os.path.join(dirpath, file)
                    date = os.path.getmtime(file_path)
                    date_norm = time.gmtime(date)
                    path = os.path.normpath(f'{date_norm.tm_year}\{date_norm.tm_mon}')
                    target_path = os.path.join(self.target_name, path)
                    os.makedirs(target_path, exist_ok=True)
                    shutil.copy2(file_path, target_path)


sorter = FileSorter(original_name='C:\lesson_009\icons',
                    target_name='C:\lesson_009\icons_by_year')
sorter.do_it()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
