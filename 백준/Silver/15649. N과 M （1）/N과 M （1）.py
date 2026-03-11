# 1~N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 사전순으로 오름차순 정렬하여 출력
# Back-Tracking
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

visited = [False] * (N + 1)
seq = []


def bt(length=0):
    if length == M:
        print(*seq)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            seq.append(i)

            bt(length + 1)

            seq.pop()
            visited[i] = False


bt()
