# python deque는 내부적으로 doubly linked list로 구현되어 있다.
from collections import deque


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = deque(map(int, input().split()))
    edits = [input().split() for _ in range(M)]

    for edit in edits:
        if edit[0] == "I":
            arr.insert(int(edit[1]), int(edit[2]))
        elif edit[0] == "D":
            del arr[int(edit[1])]
        else:  # edit[0] == 'C'
            arr[int(edit[1])] = int(edit[2])

    print(f"#{test_case} {arr[L] if L < len(arr) else -1}")
