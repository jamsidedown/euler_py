def run() -> int:
    current, product = 0, 1
    last_j, j = 0, 0
    for i in [1, 10, 100, 1000, 10_000, 100_000, 1_000_000]:
        while True:
            current += 1
            current_str = str(current)
            last_j = j
            j += len(current_str)
            if last_j < i <= j:
                product *= int(current_str[i - (last_j + 1)])
                break
    return product


if __name__ == '__main__':
    print(f'Product of nth digits: {run()}')
