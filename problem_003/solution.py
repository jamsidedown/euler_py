def run() -> int:
    last_factor, current = 1, 2
    target = 600851475143
    while target > 1:
        if target % current == 0:
            target //= current
            last_factor, current = current, 2
        else:
            current += 1 if current == 2 else 2
    return last_factor


if __name__ == '__main__':
    print(f'Largest prime factor of 600851475143: {run()}')