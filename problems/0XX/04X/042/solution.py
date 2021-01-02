from string import ascii_lowercase
from typing import List


ALPH = {c: i + 1 for i, c in enumerate(ascii_lowercase)}


def run() -> int:
    count, triangles = 0, {1}
    for word in words():
        value = word_value(word)
        while value > max(triangles):
            triangles.add(triangle(len(triangles) + 1))
        if value in triangles:
            count += 1
    return count


def triangle(n: int) -> int:
    return (n * (n + 1)) // 2


def word_value(word: str) -> int:
    return sum(ALPH[char] for char in word.lower())


def words() -> List[str]:
    with open('problems/0XX/04X/042/words.txt', 'r') as f:
        return [word.strip('"') for word in f.read().split(',')]


if __name__ == '__main__':
    print(f'Number of triangle number coded words: {run()}')
