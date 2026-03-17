import sys

input = sys.stdin.readline
N, M = map(int, input().split())
lectures = list(map(int, input().split()))

# 구해야 할 것(mid): 블루레이 크기 최솟값
left, right = max(lectures), sum(lectures)
while left <= right:
    mid = (left + right) // 2

    # 크기가 mid인 블루레이 M개 이하로 모든 강의를 순서대로 저장할 수 있는가?
    # mid가 너무 작으면 불가능(F), 충분히 크면 가능(T) -> ...FFF[T]TT...
    size, cnt = 0, 0
    for lecture in lectures:
        if size + lecture > mid:
            cnt += 1
            size = 0
        size += lecture
    if size:
        cnt += 1

    if cnt <= M:
        right = mid - 1
    else:
        left = mid + 1

print(left)
