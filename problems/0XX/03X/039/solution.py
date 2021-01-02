from typing import Dict, Set


SQUARES = {n * n: n for n in range(1, 1000)}
SQUARES_SET = set(SQUARES.keys())


def run() -> int:
    solutions: Dict[int, Set[str]] = {}

    for cc in SQUARES:
        intersection = SQUARES_SET & {cc - sq for sq in SQUARES_SET}
        for bb in intersection:
            aa = cc - bb
            c, b, a = SQUARES[cc], SQUARES[bb], SQUARES[aa]
            p = c + b + a
            if p > 1000:
                continue
            p_set = solutions.setdefault(p, set())
            p_set.add(','.join(map(str, sorted([a, b, c]))))

    solution_lens = {key: len(value) for key, value in solutions.items()}
    return max(solution_lens, key=solution_lens.get)


if __name__ == '__main__':
    print(f'Perimeter of right angle triangle with the most solutions: {run()}')
