def run() -> int:
    for c in range(998, 0, -1):
        ab = 1000 - c
        c_squared = c * c
        for b in range(ab - 1, 0, -1):
            a = ab - b
            ab_squared = a * a + b * b
            if ab_squared == c_squared:
                return a * b * c
            elif ab_squared < c_squared:
                break
    return 0


if __name__ == '__main__':
    print(f'Product of pythagorean triplet summing to 1000: {run()}')
