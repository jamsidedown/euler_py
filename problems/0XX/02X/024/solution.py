from itertools import permutations


def run() -> str:
    return list(map(''.join, permutations('0123456789')))[999_999]


if __name__ =='__main__':
    print(f'Millionth lexicographic permutation of 0-9: {run()}')