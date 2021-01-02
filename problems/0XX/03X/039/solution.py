from math import sqrt
from typing import List, Set, Union


def run() -> int:
    max_p, max_solutions = 0, 0
    for p in range(3 + 4 + 5, 1001):
        if (p_len := solutions(p)) > max_solutions:
            max_p, max_solutions = p, p_len
            print(f'{max_p}: {max_solutions}')
    return max_p


def solutions(p: int) -> int:
    valid: Set[str] = set()
    for c in range(5, p):
        csq = c * c
        for b in range(1, c):
            if b + c >= p:
                break
            bsq = b * b
            asq = csq - bsq
            a = sqrt_int(asq)
            if a is None:
                continue
            if a + b + c == p:
                valid.add(','.join(map(str, sorted([a, b, c]))))
    return len(valid)


def sqrt_int(n: int) -> Union[int, None]:
    rn = int(sqrt(n))
    if rn * rn == n:
        return rn
    if (rn + 1) * (rn + 1) == n:
        return rn + 1
    return None


if __name__ == '__main__':
    print(f'Perimeter of right angle triangle with the most solutions: {run()}')