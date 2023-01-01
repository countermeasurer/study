# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):

    def __init__(self, original_name, log_name=None):
        self.original_name = original_name
        self.log_name = log_name
        self.log_line = {}
        self.out_data = []

    @abstractmethod
    def sort_by(self):
        pass

    def read_file(self):
        with open(self.original_name, mode='r', encoding='utf8',) as original:
            for line in original:

                if line.endswith('NOK\n'):
                    if line[1:self.sort_by()] in self.log_line:
                        self.log_line[line[1:self.sort_by()]] += 1
                    else:
                        self.log_line[line[1:self.sort_by()]] = 1

    def write_file(self):

        self.out_data = sorted(parser.log_line.items(), key=lambda x: x[0])
        if self.log_name == None:
            for key in self.out_date:
                print(f'[{key[0]}]: {key[1]}')
        else:
            with open(self.log_name, mode='w', encoding='utf8') as log:
                for key in self.out_data:
                    write_data = f'[{key[0]}]:{key[1]}\n'
                    log.write(write_data)

    def do_it(self):
        self.read_file()
        self.write_file()

class ParserByMinute(Parser):

    def sort_by(self):
        self._sort_by = 17
        return self._sort_by


class ParserByHour(Parser):
    def sort_by(self):
        self._sort_by = 14
        return self._sort_by


class ParserByMonth(Parser):
    def sort_by(self):
        self._sort_by = 8
        return self._sort_by


class ParserByYear(Parser):
    def sort_by(self):
        self._sort_by = 5
        return self._sort_by


parser = ParserByHour(original_name='events.txt', log_name='events_log.txt')
parser.do_it()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
