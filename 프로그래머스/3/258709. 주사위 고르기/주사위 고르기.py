from itertools import combinations, product
from bisect import bisect_left


def solution(dices):
    win_cnt = {}
    L = len(dices)
    for A_dice_indices in combinations(range(L), L // 2):  # A: 주사위 반 선택
        B_dice_indices = [i for i in range(L) if i not in A_dice_indices]  # B: 나머지 반 선택

        # 만들 수 있는 모든 주사위 조합의 합 구하기
        A, B = [], []
        for dice_face_indices in product(range(6), repeat=L // 2):
            A.append(sum(dices[i][j] for i, j in zip(A_dice_indices, dice_face_indices)))
            B.append(sum(dices[i][j] for i, j in zip(B_dice_indices, dice_face_indices)))
        B.sort()  # 이진 탐색을 위해 정렬

        # bisect_left로 얻은 인덱스 = A가 이길 수 있는 경우의 수
        wins = sum(bisect_left(B, num) for num in A)
        win_cnt[wins] = list(A_dice_indices)

    max_key = max(win_cnt.keys())

    return [x + 1 for x in win_cnt[max_key]]
