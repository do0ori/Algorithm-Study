# 1 2 3 4 5가 각각 5개씩 존재, 1에만 색종이 사용 가능
# 모든 1을 덮는 데 필요한 색종이의 최소 개수 출력
# 1을 모두 덮지 못할 경우에는 -1을 출력
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

board = [list(map(int, input().split())) for _ in range(10)]
paper = [5] * 5


def can_attach(r, c, size):
    # 범위 안에 존재하는지 확인
    if r + size > 10 or c + size > 10:
        return False

    # 범위 내 칸 값이 모두 1인지 확인
    for i in range(r, r + size):
        for j in range(c, c + size):
            if board[i][j] != 1:
                return False

    return True


def fill(r, c, size, value):
    for i in range(r, r + size):
        for j in range(c, c + size):
            board[i][j] = value


def bt(pos, total, min_total=float("inf")):
    # 가지치기
    if min_total <= total:
        return min_total

    # 종료 조건
    if pos == 100:
        return min(min_total, total)

    r, c = divmod(pos, 10)
    if board[r][c]:
        # 색종이 붙이기
        for size in range(5, 0, -1):
            if paper[size - 1] != 0 and can_attach(r, c, size):
                paper[size - 1] -= 1
                fill(r, c, size, 0)

                min_total = bt(pos + 1, total + 1, min_total)

                paper[size - 1] += 1
                fill(r, c, size, 1)
            else:
                continue
    else:
        min_total = bt(pos + 1, total, min_total)

    return min_total


min_total = bt(0, 0)
print(-1 if min_total == float("inf") else min_total)
