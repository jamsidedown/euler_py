from typing import List


def run() -> int:
    i, n = 1, 1
    while len(factors(n)) < 500:
        i += 1
        n = sum(range(i + 1))
    return n


def factors(n: int) -> List[int]:
    f, i = [], 1
    while i * i <= n:
        if n % i == 0:
            f += list({i, n // i})
        i += 1
    return f


if __name__ == '__main__':
    print(f'First triangular number with over 500 divisors: {run()}')
