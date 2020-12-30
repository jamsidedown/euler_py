from math import prod
from typing import Iterator


def run() -> int:
    last = prod(range(1, 21))
    current = last
    for factor in get_factors(last):
        while all(current % value == 0 for value in range(1, 21)):
            last = current
            if current % factor == 0:
                current //= factor
        else:
            current = last
    return current


def get_factors(n: int) -> Iterator[int]:
    target, current = n, 2
    while target > 1:
        if target % current == 0:
            yield current
            while target % current == 0:
                target //= current
        current += 1 if current == 2 else 2
    return


if __name__ == '__main__':
    print(f'Smallest positive number evenly divisible by 1-20: {run()}')
