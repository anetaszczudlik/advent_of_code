from pathlib import Path

is_test = True


def read_file():
    file = Path(f'data/02{"-test"if is_test else ""}.txt')
    file.touch(exist_ok=True)
    return file.read_text()


def part_one():
    # win - 8
    # lose - 1
    # draw - 3
    # A - rock, B - paper , C - scisors
    moves = read_file().split('\n')
    result = 0
    for move in moves:
        oponent, gamer = move.split(' ')
        if oponent == 'A':  # ROCK
            if gamer == 'X':
                result += 6
            if gamer == 'Y':
                result += 8
            if gamer == 'Z':
                result += 1
        if oponent == 'B':  # PAPER
            if gamer == 'X':
                result += 1
            if gamer == 'Y':
                result += 6
            if gamer == 'Z':
                result += 8
        if oponent == 'C':  # SCISSORS
            if gamer == 'X':
                result += 8
            if gamer == 'Y':
                result += 1
            if gamer == 'Z':
                result += 6
    return result


def part_two():

    return None


if __name__ == '__main__':
    result_one = part_one()
    if is_test:
        assert result_one == 15
        print('part one pass!!!')
    print(result_one)
    result_two = part_two()
    if is_test:
        assert result_two == 12
        print('part two pass!!!')
    print(result_two)
