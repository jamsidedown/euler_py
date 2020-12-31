def run() -> int:
    total = 0
    i = 10
    powers = {str(x): x**5 for x in range(10)}
    while i < 1_000_000:
        value = sum(powers[d] for d in str(i))
        if value == i:
            total += value
        i += 1
    return total


if __name__ == '__main__':
    print(f'Sum of numbers that can be written as the sum of their digits\' fifth powers: {run()}')
