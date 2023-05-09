

class WrongSymbols(Exception):
    pass


class SumError(Exception):
    pass


def check_frames(frames):
    step = 0
    count_frames = 0
    count_x = 0
    prev_symbol = 'f'
    for symbol in frames:
        step += 1
        if step % 2 != 0:
            if symbol == 'X':
                count_x += 1
                count_frames += 1
                step -= 1
            elif symbol == '/':
                raise Exception('Первый символ фрейма /')
            elif not symbol.isdigit() and  symbol != '-' and symbol != 'X':
                raise WrongSymbols(f'Неверный символ {symbol}')
            elif symbol == 0:
                raise WrongSymbols(f'Неверный символ {symbol}')


