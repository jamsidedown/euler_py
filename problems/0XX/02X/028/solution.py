from typing import List


def run() -> int:
    total = 0
    for i in range(1, 1002, 2):
        total += sum(corners(i))
    return total


def corners(size: int) -> List[int]:
    if size == 1:
        return [1]
    size_sq = size * size
    size_m1 = size - 1
    return [
        size_sq,
        size_sq - size_m1,
        size_sq - (2 * size_m1),
        size_sq - (3 * size_m1)
    ]


if __name__ == '__main__':
    print(f'Sum of diagonals in 1001x1001 spiral: {run()}')