def run() -> int:
    sum_of_squares = sum(x ** 2 for x in range(1, 101))
    square_of_sums = sum(range(1, 101)) ** 2
    return square_of_sums - sum_of_squares


if __name__ == '__main__':
    print(f'Difference of the sum of the squares and square of the sums of the first 100 natural numbers: {run()}')