def run() -> int:
    max_primes_count = 0
    max_a, max_b = 0, 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            if (count := primes_count(a, b)) > max_primes_count:
                max_primes_count = count
                max_a, max_b = a, b
    return max_a * max_b


def primes_count(a: int, b: int) -> int:
    n = 0
    while True:
        if not is_prime((n * n) + (a * n) + b):
            break
        n += 1
    return n


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1 + (i > 2)
    return True


if __name__ == '__main__':
    print(f'Product of parameters giving most consecutive primes: {run()}')
