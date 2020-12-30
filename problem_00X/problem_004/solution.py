def run() -> int:
    palindromes = []
    for x in range(999, 99, -1):
        for y in range(x, 99, -1):
            xy = x * y
            xys = str(xy)
            if xys == xys[::-1]:
                palindromes.append(xy)
    return max(palindromes)


if __name__ == '__main__':
    print(f'Largest palindromic product of two 3-digit numbers: {run()}')