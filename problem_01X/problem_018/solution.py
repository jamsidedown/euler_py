from os import truncate
from typing import List


def run() -> int:
    triangle = parse()[::-1]
    height = len(triangle)
    for y in range(1, height):
        for x in range(height - y):
            triangle[y][x] += max(triangle[y - 1][x:x + 2])
    return triangle[::-1][0][0]


def parse() -> List[List[int]]:
    with open('problem_01X/problem_018/input.txt', 'r') as f:
        return [[int(value.lstrip('0') or '0') for value in line.split()] for line in f]


if __name__ == '__main__':
    print(f'Maximum path through triangle: {run()}')