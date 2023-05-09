import os, bowling

winner_in_tour = {}
info_to_out = []


def score_tournament(in_file, out_file):
    with open(os.path.join(in_file), encoding='utf-8') as file_in:
        for line in file_in:
            if line.startswith('###') or len(line) == 1:
                info_to_out.append(line[:-1])
            elif line.startswith('winner'):
                info_to_out.append(f'Winner is {winner_in_tour[max(winner_in_tour)]}')
                winner_in_tour.clear()
            else:
                line = line.split()
                try:
                    get_score_name = bowling.get_score(get_string=line[1])
                except (Exception, bowling.SumError, bowling.WrongSymbols) as exc:
                    winner_in_tour[0] = line[0]
                    info_to_out.append(f'{line[0]} {line[1]} 0 => {exc}')
                else:
                    winner_in_tour[get_score_name] = line[0]
                    info_to_out.append(f'{line[0]} {line[1]} {get_score_name}')

    with open(os.path.join(out_file), mode='a', encoding='utf-8') as file_out:
        for line in info_to_out:
            file_out.write(line + '\n')



def score_tournament_europe(in_file, out_file):
    with open(os.path.join(in_file), encoding='utd-8') as file_in:
        for line in file_in:
            if line.startswith('###') or len(line) == 1:
                info_to_out.append(line[-1])
            elif line.startswith('winner'):
                info_to_out.append(f'Winner id {winner_in_tour[max(winner_in_tour)]}')
                winner_in_tour.clear()
            else:
                line = line.split()
                try:
                    get_score_name = bowling.get_score_europe(get_string=line[1])
                except (Exception, bowling.SumError, bowling.WrongSymbols) as exc:
                    winner_in_tour[0] = line[0]
                    info_to_out.append(f'{line[0]} {line[1]} 0 => {exc}')
                else:
                    winner_in_tour[get_score_name] = line[0]
                    info_to_out.append(f'{line[0]} {line[1]} {get_score_name}')


    with open(os.path.join(out_file), mode='a', encoding='utf-8') as file_out:
        for line in info_to_out:
            file_out.write(line + '\n')
