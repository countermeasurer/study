class WrongSymbol(Exception):
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
                raise Exception('Первый символ фрейма "/" ')
            elif not symbol.isdigit() and symbol != '-' and symbol != 'X':
                raise WrongSymbol(f'Неверный символ {symbol} ')
            elif symbol == '0':
                raise WrongSymbol(f'Неверный символ {symbol} ')
        elif step % 2 == 0:
            count_frames += 1
            if symbol == 'X':
                raise Exception('Второй символ фрейма "Х" ')
            elif not symbol.isdigit() and symbol != '-' and symbol != '/':
                raise WrongSymbol(f'Неверный символ {symbol} ')
            elif symbol == '0':
                raise WrongSymbol(f'Неверный символ {symbol} ')
            elif prev_symbol.isdigit() and symbol.isdigit() and int(prev_symbol) + int(symbol) >= 10:
                raise SumError(f'Неверный ввод, либо сумма > 10  ({prev_symbol}, {symbol})')
        prev_symbol = symbol
    if (len(frames) + count_x) / 2 != 10:
        raise Exception('Количество фреймов != 10 (лишний/не хватает сомволов)')


def get_score(get_string):
    score_prepare = []
    check_frames(frames=get_string)
    for x in range(0, len(get_string)):
        if get_string[x] == 'X':
            score_prepare.append(20)
        elif get_string[x] == '-':
            score_prepare.append(0)
        elif get_string[x].isdigit():
            score_prepare.append(int(get_string[x]))
        elif get_string[x] == '/':
            score_prepare.append(15)
            score_prepare.pop(-2)
    return sum(score_prepare)


def get_score_europe(get_string):
    score_prepare = []
    spar_and_strike = []
    check_frames(frames=get_string)
    for x in range(0, len(get_string)):
        if get_string[x] == 'X':
            score_prepare.append(11)
        elif get_string[x] == '-':
            score_prepare.append(0)
        elif get_string[x] == '/':
            score_prepare[-1] = 10
        elif get_string[x].isdigit():
            score_prepare.append(int(get_string[x]))
    for i in range(len(score_prepare)):
        if score_prepare[i] == 10:
            if i+1 < len(score_prepare):
                spar_and_strike.append(score_prepare[i+1])
            else:
                if i+1 == len(score_prepare):
                    spar_and_strike.append(10)
        if score_prepare[i] == 11:
            if i+1 < len(score_prepare):
                spar_and_strike.append(score_prepare[i+1])
            else:
                if i+1 == len(score_prepare):
                    spar_and_strike.append(10)
            if i+2 < len(score_prepare):
                spar_and_strike.append(score_prepare[i+2])
            else:
                if i+2 == len(score_prepare):
                    spar_and_strike.append(10)
    score_result = sum(spar_and_strike) + sum(score_prepare)
    return score_result


get_score_europe(get_string='4/81X3/4/1/-12651X')
get_score_europe(get_string='811/X--3/XX171/43')
get_score_europe(get_string='X34--3/4353-5--629/')


