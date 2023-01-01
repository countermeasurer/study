# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile


class StatCounter:
    def __init__(self, file_name, sort_method='Ascending'):
        self.file_name = file_name
        self.stat = {}
        self.sort_method = sort_method
        self.total_counter = 0

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect_stat(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1
                        self.total_counter += 1

    def sorting(self):
        self.sorted_stat = []
        for key, value in self.stat.items():
            self.sorted_stat.append([key, value])
        match self.sort_method:
            case 'Ascending':
                self.sorted_stat.sort(key=lambda val: val[1], reverse=False)
            case 'Descending':
                self.sorted_stat.sort(key=lambda val: val[1], reverse=True)
            case 'abcAscending':
                self.sorted_stat.sort(key=lambda val: val[0], reverse=False)
            case 'abcDescending':
                self.sorted_stat.sort(key=lambda val: val[0], reverse=True)

    def do_it(self):
        self.collect_stat()
        self.sorting()
        print(f"+{'+':-^30}+")
        print(f"|{'Буква':^14}|" + f"{'Частота':^15}|")
        print(f"+{'+':-^30}+")
        for val in self.sorted_stat:
            print(f"|{val[0]:^14}|" + f"{val[1]:^15}|")
        print(f"+{'+':-^30}+")
        print(f"|{'ИТОГО':^14}|" + f"{self.total_counter:^15}|")
        print(f"+{'+':-^30}+")

counter = StatCounter(file_name='voyna-i-mir.txt.zip', sort_method='Ascending')

counter.do_it()