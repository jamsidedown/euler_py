def run() -> int:
    total, first, second = 0, 1, 2
    while second < 4_000_000:
        if second % 2 == 0:
            total += second
        first, second = second, first + second
    return total


if __name__ == '__main__':
    print(f'Sum of even fibonacci numbers under 4M: {run()}')
