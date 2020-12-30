from math import prod
from operator import pos
from typing import List


def run() -> int:
    abundant = [n for n in range(12, 28124) if n < sum(divisors(n))]
    possible = {a + b for i, a in enumerate(abundant) for b in abundant[i:]}
    possible = {p for p in possible if p < 28124}
    impossible = set(range(1, 28124)) - possible
    return sum(impossible)


def divisors(n: int) -> List[int]:
    f, i = [1], 2
    while i * i <= n:
        if n % i == 0:
            f += list({i, n // i})
        i += 1
    return f


if __name__ == '__main__':
    print(f'Sum of all positive integers which can\'t be written as the sum of two adundant numbers: {run()}')