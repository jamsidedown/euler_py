from math import prod


def run() -> int:
    number = parse()
    return max(prod(int(digit) for digit in number[start:start + 13]) for start in range(len(number) - 13))


def parse() -> str:
    with open('problem_008/input.txt', 'r') as f:
        return f.read().replace('\n', '')


if __name__ == '__main__':
    print(f'Greatest product of 13 adjacent numbers: {run()}')