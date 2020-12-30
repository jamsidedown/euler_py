from functools import lru_cache


SIZE = 20


def run() -> int:
    return paths(0, 0)


@lru_cache
def paths(x: int, y: int) -> int:
    if x > SIZE or y > SIZE:
        return 0
    if x == SIZE and y == SIZE:
        return 1
    return paths(x + 1, y) + paths(x, y + 1)


if __name__ == '__main__':
    print(f'Routes through {SIZE}x{SIZE} grid: {run()}')
