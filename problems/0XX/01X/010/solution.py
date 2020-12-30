from math import sqrt


def run() -> int:
    sieve = {2: True, **{x: True for x in range(3, 2_000_000, 2)}}
    factors = [2] + list(range(3, int(sqrt(2_000_000)), 2))

    for prime in factors:
        if sieve.get(prime, False):
            current = prime * prime
            while current < 2_000_000:
                if sieve.get(current, False):
                    sieve[current] = False
                current += prime

    return sum(p for p in sieve if sieve[p])


if __name__ == '__main__':
    print(f'Sum of primes below 2M: {run()}')