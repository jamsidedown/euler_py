from functools import lru_cache
from typing import List


COINS = [200, 100, 50, 20, 10, 5, 2, 1]


def run() -> int:
    return len(combinations(200))


@lru_cache(maxsize=512)
def combinations(value: int, last: int = 200) -> List[str]:
    combs = []
    for coin in [c for c in COINS if c <= value and c <= last]:
        if coin == value:
            combs.append(str(coin))
        else:
            combs += [f'{coin},{comb}' for comb in combinations(value - coin, coin)]
    return combs


if __name__ == '__main__':
    print(f'Number of different ways to make £2: {run()}')
