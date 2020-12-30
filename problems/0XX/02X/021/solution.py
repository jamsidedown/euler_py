from typing import List


def run() -> int:
    amicable = []
    for x in range(2, 10_000):
        divisors = factors(x)
        y = sum(divisors)
        if x != y and sum(factors(y)) == x:
            amicable += [x, y]
    return sum(set(amicable))


def factors(n: int) -> List[int]:
    f, i = [1], 2
    while i * i <= n:
        if n % i == 0:
            f += list({i, n // i})
        i += 1
    return f


if __name__ == '__main__':
    print(f'Sum of amicable numbers under 10_000: {run()}')
