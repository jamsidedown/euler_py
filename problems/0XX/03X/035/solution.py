from math import sqrt


def run() -> int:
    return sum(
        all(is_prime(int(num[i:] + num[0:i])) for i in range(len(num)))
        for num in map(str, range(1_000_000))
    )


def is_prime(n: int) -> bool:
    if n < 3:
        return n == 2
    return n % 2 and all(n % i > 0 for i in range(3, int(sqrt(n)) + 1, 2))


if __name__ == '__main__':
    print(f'Number of circular primes below 1M: {run()}')
