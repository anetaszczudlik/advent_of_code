from pathlib import Path

is_test = False


def read_file():
    file = Path(f'data/01{"-test"if is_test else ""}.txt')
    file.touch(exist_ok=True)
    return file.read_text()


def parse_elfs():
    return [
        sum([int(snack) for snack in elf.split('\n')])
        for elf in read_file().split('\n\n')
    ]


def part_one():
    elfs = parse_elfs()
    return max(elfs)


def part_two():
    elfs = parse_elfs()
    elfs.sort(reverse=True)
    return elfs[0] + elfs[1] + elfs[2]


if __name__ == '__main__':
    result_one = part_one()
    if is_test:
        assert result_one == 24000
        print('part one pass!!!')
    print(result_one)
    result_two = part_two()
    if is_test:
        assert result_two == 45000
        print('part two pass!!!')
    print(result_two)
