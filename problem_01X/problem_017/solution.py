DIGITS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'
}

TEENS = {
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'
}

TENS = {
    10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
}

LIMIT = 1000


def run() -> int:
    return sum(len(to_string(n).replace(' ', '')) for n in range(1, LIMIT + 1))


def to_string(n: int) -> str:
    if n == 1000:
        return 'one thousand'

    result = ''
    if hundreds := n // 100:
        result = f'{DIGITS[hundreds]} hundred'
        n %= 100
        if n:
            result = f'{result} and'

    if 10 < n < 20:
        result = f'{result} {TEENS[n]}'
        n = 0

    if tens := n // 10:
        result = f'{result} {TENS[tens * 10]}'
        n %= 10

    if n:
        result = f'{result} {DIGITS[n]}'

    return result.strip()


if __name__ == '__main__':
    print(f'Total length of words 1-1000: {run()}')
