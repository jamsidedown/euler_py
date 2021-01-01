from typing import List


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


def get_numbers(limit: int) -> List[int]:
    ns = []
    for i in range(2, limit + 1):
        s = str(i)
        if len(set(s)) == len(s):
            ns.append(i)
    return ns


if __name__ == '__main__':
    print(f'Sum of pandigital products: {run()}')