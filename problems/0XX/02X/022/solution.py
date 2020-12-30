from string import ascii_lowercase
from typing import List


ALPH = {char: i + 1 for i, char in enumerate(ascii_lowercase)}


def run() -> int:
    return sum((i + 1) * score(name) for i, name in enumerate(parse()))


def score(name: str) -> int:
    return sum(ALPH[char] for char in name)


def parse() -> List[str]:
    with open('problems/0XX/02X/022/names.txt', 'r') as f:
        return list(sorted(name.strip('"').lower() for name in f.read().split(',')))


if __name__ == '__main__':
    print(f'Sum of name scores: {run()}')
