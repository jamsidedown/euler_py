MONTHS = {
    0: 31, 1: 28, 2: 31, 3: 30, 4: 31, 5: 30, 6: 31, 7: 31, 8: 30, 9: 31, 10: 30, 11: 31
}


def run() -> int:
    # 1st Jan 1900 is a Monday (0th day)
    day, count = 0, 0
    for year in range(1900, 2001):
        is_leap = leap(year)
        for month in range(12):
            if year > 1900 and day == 6:
                count += 1
            days_in_month = MONTHS[month]
            if is_leap and month == 1:
                days_in_month += 1
            day = (day + days_in_month) % 7
    return count


def leap(n: int) -> bool:
    return n % 400 == 0 if n % 100 == 0 else n % 4 == 0


if __name__ == '__main__':
    print(f'Sundays on the 1st of the month in the 20th century: {run()}')