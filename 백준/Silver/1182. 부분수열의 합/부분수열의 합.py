import sys

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

answer = 0
visited = [False] * N


def dfs(l=0, s=0):
    global answer

    if l == N:
        if s == S:
            answer += 1
        return

    dfs(l + 1, s)

    visited[l] = True
    dfs(l + 1, s + A[l])
    visited[l] = False


dfs()
# S가 0이면 아무것도 고르지 않은 경우에도 충족되므로 1 빼주기
print(answer if S != 0 else answer - 1)
