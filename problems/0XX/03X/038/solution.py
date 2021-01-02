DIGITS = {str(n) for n in range(1, 10)}


def run() -> int:
    max_pan = 0
    for x in range(1, 9999):
        n = str(x)
        for y in range(2, 10):
            n += str(x * y)
            if len(n) > 9:
                break
            if pandigital(n):
                max_pan = max(max_pan, int(n))
    return max_pan


def pandigital(n: str) -> bool:
    return len(n) == 9 and set(n) == DIGITS


if __name__ == '__main__':
    print(f'Largest pandigital 9 digit number: {run()}')