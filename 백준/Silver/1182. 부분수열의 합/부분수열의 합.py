import sys

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

answer = 0


def dfs(l=0, s=0, cnt=0):
    global answer

    if l == N:
        if s == S and cnt > 0:
            answer += 1
        return

    dfs(l + 1, s, cnt)  # 선택 O
    dfs(l + 1, s + A[l], cnt + 1)  # 선택 X


dfs()
print(answer)
