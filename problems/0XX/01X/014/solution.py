from functools import lru_cache
from typing import List


def run() -> int:
    max_i, max_length = 0, 0
    for i in range(1, 1_000_000):
        collatz_length = len(collatz(i))
        if collatz_length > max_length:
            max_i, max_length = i, collatz_length
    return max_i


@lru_cache(maxsize=1024)
def collatz(n: int) -> List[int]:
    return [1] if n == 1 else [n] + collatz(n // 2 if n % 2 == 0 else (3 * n) + 1)


if __name__ == '__main__':
    print(f'Longest Collatz sequence start under 1M: {run()}')