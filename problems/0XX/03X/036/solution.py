def run() -> int:
    return sum(n for n in range(1_000_000) if is_palindrome(n))


def is_palindrome(n: int) -> bool:
    return (ns := str(n)) == ns[::-1] and (nbs := f'{n:b}') == nbs[::-1]


if __name__ == '__main__':
    print(f'Sum of double base palindromes under 1M: {run()}')
