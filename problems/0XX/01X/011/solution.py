from math import prod
from typing import List


def run() -> int:
    grid = parse()
    height, width = len(grid), len(grid[0])
    horizontal = max(prod(line[x:x + 4]) for line in grid for x in range(width - 4))
    vertical = max(prod(line[x] for line in grid[y:y + 4]) for y in range(height - 4) for x in range(width))
    diag_right = max(prod(grid[y + i][x + i] for i in range(4)) for y in range(height - 4) for x in range(width - 4))
    diag_left = max(prod(grid[y + i][x - i] for i in range(4)) for y in range(height - 4) for x in range(3, width))
    return max(horizontal, vertical, diag_right, diag_left)


def parse() -> List[List[int]]:
    with open('problems/0XX/01X/011/input.txt', 'r') as f:
        return [[int(value.lstrip('0') or '0') for value in line.split()] for line in f]


if __name__ == '__main__':
    print(f'Largest product of 4 adjacent numbers: {run()}')