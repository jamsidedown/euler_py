from fractions import Fraction
from functools import reduce
from operator import mul
from typing import List


def run() -> int:
    fs: List[Fraction] = []
    for n in map(str, range(10, 100)):
        for d in [str(d) for d in range(int(n) + 1, 100) if d % 10 > 0]:
            if n[1] == d[0] and (f := Fraction(f'{n}/{d}')) == Fraction(f'{n[0]}/{d[1]}'):
                fs.append(f)
    return reduce(mul, fs).denominator


if __name__ == '__main__':
    print(f'Denominator of product of four non-trivial examples: {run()}')
