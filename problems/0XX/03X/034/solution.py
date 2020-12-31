from math import factorial


DIGITS = {str(x): factorial(x) for x in range(10)}


def run() -> int:
    # 9! * 7 = 2540160
    # 9! * 8 = 2903040
    # max 7 digits before a number cannot equal the sum of its digits' factorials
    return sum(n for n in range(10, factorial(9) * 7) if n == sum(DIGITS[d] for d in str(n)))


if __name__ == '__main__':
    print(f'Sum of numbers equal to sum of their digits\' factorials: {run()}')
