from typing import List


def run() -> str:
    return str(sum(parse()))[:10]


def parse() -> List[int]:
    with open('problem_013/input.txt', 'r') as f:
        return [int(line.strip()) for line in f]


if __name__ == '__main__':
    print(f'First 10 digits of sum: {run()}')