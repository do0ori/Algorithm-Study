def solution(contests, k: int, p: int):
    ranked = []

    for idx, contest in enumerate(contests):
        solvable = sum(1 for difficulty in contest if difficulty <= p)
        ranked.append((-solvable, idx))

    ranked.sort()
    selected = sorted(idx for _, idx in ranked[:k])
    return selected
