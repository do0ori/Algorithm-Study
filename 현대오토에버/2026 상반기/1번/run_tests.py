from itertools import permutations

from 방문_블록_최소_이동_거리 import solution as solution1

# =========================
# Problem 1 helpers
# =========================


def brute_problem1(w, h, targets):
    def to_pos(x):
        x -= 1
        return x // w, x % w

    def md(a, b):
        r1, c1 = to_pos(a)
        r2, c2 = to_pos(b)
        return abs(r1 - r2) + abs(c1 - c2)

    others = [x for x in targets if x != 1]
    best = float("inf")

    for order in permutations(others):
        total = 0
        cur = 1
        for x in order:
            total += md(cur, x)
            cur = x
        best = min(best, total)

    return 0 if not others else best


# =========================
# Tests
# =========================


def test_problem1():
    cases = [
        (5, 2, [1], 0),
        (5, 2, [1, 4], 3),
        (5, 2, [1, 6], 1),
        (5, 2, [1, 4, 6, 10], 7),
        (3, 3, [1, 3, 5, 9], None),
    ]

    print("=== Problem 1 ===")
    for w, h, targets, expected in cases:
        ans = solution1(w, h, targets)
        if expected is None:
            expected = brute_problem1(w, h, targets)
        print(f"w={w}, h={h}, targets={targets} -> ans={ans}, expected={expected}")
        assert ans == expected
    print("Problem 1 passed.\n")


if __name__ == "__main__":
    test_problem1()
    print("All tests passed!")
