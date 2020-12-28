def run() -> int:
    factors = set()
    target = 600851475143
    i = 2
    while i * i <= target:
        if target % i == 0:
            factors.add(i)
            factors.add(target / i)
        i += 1

    return max(filter(is_prime, factors))


def is_prime(n: int) -> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


if __name__ == '__main__':
    print(f'Largest prime factor of 600851475143: {run()}')