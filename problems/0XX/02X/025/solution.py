from math import log10


def run() -> int:
    first, second, index = 1, 1, 2
    while log10(second) < 999:
        first, second, index = second, first + second, index + 1
    return index


if __name__ == '__main__':
    print(f'Index of first 1000 digit fibonacci number: {run()}')
