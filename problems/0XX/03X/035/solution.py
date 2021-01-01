def run() -> int:
    return sum(
        all(is_prime(int(num[i:] + num[0:i])) for i in range(len(num)))
        for num in map(str, range(1_000_000))
    )


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
    print(f'Number of circular primes below 1M: {run()}')
