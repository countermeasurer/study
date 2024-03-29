# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#

import os
import threading


class FileTreatment(threading.Thread):

    def __init__(self, path, lock, not_zero_volatility, zero_volatility, *args, **kwargs):
        super(FileTreatment, self).__init__(*args, **kwargs)
        self.path = path
        self.volatility = None
        self.ticker = None
        self.lock_flow = lock
        self.not_zero_volatility_list = not_zero_volatility
        self.zero_volatility_list = zero_volatility

    def run(self):
        with open(self.path) as read_file:
            self.unpacking_file(read_file)
        with self.lock_flow:
            if self.volatility == 0:
                self.zero_volatility_list.append(self.ticker)
            else:
                self.not_zero_volatility_list.append((self.volatility, self.ticker))

    def unpacking_file(self, read_file):
        minimum_value = None
        maximum_value = None
        is_first_line = True
        for _, line in enumerate(read_file):
            if is_first_line:
                is_first_line = False
            else:
                self.ticker, trade_time, price, quantity = line.split(',')
                check_price = float(price)
                if minimum_value is None:
                    minimum_value = check_price
                    maximum_value = check_price
                elif minimum_value > check_price:
                    minimum_value = check_price
                elif maximum_value < check_price:
                    maximum_value = check_price
        self.calculations_file_and_sorted(maximum_value, minimum_value)

    def calculations_file_and_sorted(self, maximum_value, minimum_value):
        if maximum_value is None or minimum_value is None:
            raise ValueError('ERROR')
        else:
            average_price = (maximum_value + minimum_value) / 2
            self.volatility = round(((maximum_value - minimum_value) / average_price) * 100, 2)


def main():
    zero_volatility = []
    all_volatility = []
    flows = []
    lock = threading.Lock()
    for dirpath, _, filenames in os.walk('trades'):
        for file in filenames:
            path = os.path.join(dirpath, file)
            flow = FileTreatment(path, lock, all_volatility, zero_volatility)
            flows.append(flow)

    for elem in flows:
        elem.start()

    for elem in flows:
        elem.join()

    all_volatility.sort(reverse=True)
    zero_volatility.sort()
    max_volatility = all_volatility[0:3]
    min_volatility = all_volatility[-3::]
    print('max:')
    for element in max_volatility:
        print(element)
    print('Min')
    for element in min_volatility:
        print(element)
    print('zero:')
    print(zero_volatility)


if __name__ == '__main__':
    main()

