from itertools import combinations, permutations

from 적을_k명_처치하기_위한_최소_초기_체력 import solution as solution2

# =========================
# Problem 2 helpers
# =========================


def can_kill_order(order, initial_health):
    h = initial_health
    if h <= 0:
        return False
    for p in order:
        if h <= p:
            return False
        h += p
        if h <= 0:
            return False
    return True


def brute_problem2(powers):
    n = len(powers)
    answer = []

    for k in range(1, n + 1):
        best = None
        for subset in combinations(range(n), k):
            for perm in permutations(subset):
                order = [powers[i] for i in perm]

                lo, hi = 1, 200
                while lo < hi:
                    mid = (lo + hi) // 2
                    if can_kill_order(order, mid):
                        hi = mid
                    else:
                        lo = mid + 1
                need = lo

                if best is None or need < best:
                    best = need

        answer.append(best)
    return answer


# =========================
# Tests
# =========================


def test_problem2():
    cases = [
        ([1], [2]),
        ([-1], [2]),
        ([2, -1], [2, 3]),
        ([3, 4, -2], [3, 4, 4]),
        ([1, 2, -1], None),
        ([2, 5, -1, -2], None),
    ]

    print("=== Problem 2 ===")
    for powers, expected in cases:
        ans = solution2(powers)
        if expected is None:
            expected = brute_problem2(powers)
        print(f"powers={powers} -> ans={ans}, expected={expected}")
        assert ans == expected
    print("Problem 2 passed.\n")


if __name__ == "__main__":
    test_problem2()
    print("All tests passed!")
