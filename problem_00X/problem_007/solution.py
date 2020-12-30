def run() -> int:
    primes = [2]
    current = 3
    while len(primes) < 10_001:
        if all(current % p > 0 for p in primes if p * p <= current):
            primes.append(current)
        current += 2
    return primes[-1]


if __name__ == '__main__':
    print(f'10_001st prime: {run()}')
