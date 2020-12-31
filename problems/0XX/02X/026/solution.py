def run() -> int:
    max_denominator, max_recurring_cycle = 1, 0
    for i in range(2, 1000):
        if (cycle_length := recurring_cycle(i)) > max_recurring_cycle:
            max_denominator, max_recurring_cycle = i, cycle_length
    return max_denominator


def recurring_cycle(n: int) -> int:
    result = '.'
    remainder = 10
    index = 0
    remainders = {}
    while remainder > 0:
        result = f'{result}{remainder // n}'
        remainder = (remainder % n) * 10
        if remainder in remainders:
            return index - remainders[remainder]
        remainders[remainder] = index
        index += 1
    return 0


if __name__ == '__main__':
    print(f'Value of d with the longest recurring cycle in it\'s decimal fraction: {run()}')
