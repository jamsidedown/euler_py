from itertools import permutations
from math import sqrt


ENDS = [1, 3, 7, 9]


def run() -> int:
    largest_prime = 0
    for n in range(3, 10):
        digits = ''.join(map(str, range(1, n + 1)))
        for end in [i for i in ENDS if i <= n]:
            for xs in map(''.join, permutations(digits.replace(str(end), ''))):
                if (x := int(xs + str(end))) > largest_prime and is_prime(x):
                    largest_prime = x
    return largest_prime


def is_prime(n: int) -> bool:
    if n < 3:
        return n == 2
    return n % 2 and all(n % i > 0 for i in range(3, int(sqrt(n)) + 1, 2))


if __name__ == '__main__':
    print(f'Largest n-digit pandigital prime: {run()}')