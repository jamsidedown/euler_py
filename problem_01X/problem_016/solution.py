def run() -> int:
    return sum(int(char) for char in str(2**1000))


if __name__ == '__main__':
    print(f'Sum of digits in 2**1000: {run()}')