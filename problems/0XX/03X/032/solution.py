from typing import Iterator, List


DIGITS = set('123456789')


def run() -> int:
    products = set()
    nums = get_numbers(10_000)
    nums_set, nums_max = set(nums), max(nums)
    for i in range(len(nums) - 1):
        a = nums[i]
        if a * a > nums_max:
            break
        a_set = set(str(a))
        for b in nums[i + 1:]:
            b_set = set(str(b))
            if a_set & b_set:
                continue
            c = a * b
            if c > nums_max:
                break
            if c not in nums_set:
                continue
            c_set = set(str(c))
            if (a_set | b_set) & c_set:
                continue
            if (a_set | b_set | c_set) == DIGITS:
                products.add(c)
    return sum(products)


def run_old() -> int:
    products = set()
    for a in range(2, 10_000):
        a_str = str(a)
        a_set = set(a_str)
        a_len = len(a_str)
        if len(a_set) != a_len:
            continue
        b_start = a + 1
        for b in range(b_start, 100_000):
            b_str = str(b)
            b_set = set(b_str)
            b_len = len(b_str)
            if len(b_set) != b_len:
                continue
            ab_set = a_set | b_set
            ab_len = a_len + b_len
            if a_set & b_set:
                continue
            c = a * b
            c_str = str(c)
            c_set = set(c_str)
            c_len = len(c_str)
            abc_set = ab_set | c_set
            abc_len = ab_len + c_len
            if abc_len > 10:
                break
            if ab_set & c_set:
                continue
            if abc_set == DIGITS:
                products.add(c)
    return sum(products)


def get_numbers(limit: int) -> List[int]:
    ns = []
    for i in range(2, limit + 1):
        s = str(i)
        if len(set(s)) == len(s):
            ns.append(i)
    return ns


if __name__ == '__main__':
    print(f'Sum of pandigital products: {run()}')