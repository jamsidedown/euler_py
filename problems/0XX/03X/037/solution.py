from math import sqrt


def run() -> int:
    return sum(n for n in range(10, 1_000_000) if is_truncatable_prime(n))


def is_truncatable_prime(n: int) -> bool:
    if not is_prime(n):
        return False
    ns, lns = str(n), len(str(n))
    return all(is_prime(int(ns[i:])) and is_prime(int(ns[:lns - i])) for i in range(1, lns))


def is_prime(n: int) -> bool:
    if n < 3:
        return n == 2
    return n % 2 and all(n % i > 0 for i in range(3, int(sqrt(n)) + 1, 2))


if __name__ == '__main__':
    print(f'Sum of reverse truncatable primes: {run()}')
