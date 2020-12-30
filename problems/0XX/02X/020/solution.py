from math import factorial


def run() -> int:
    return sum(int(digit) for digit in str(factorial(100)))


if __name__ == '__main__':
    print(f'Sum of digits in 100! : {run()}')
