# List를 이용한 Binary Tree 표현하기: 완전 이진 트리 - 중위 순회 (Left -> Root -> Right)
def make_tree(i):
    global number

    # 분할 정복
    if i <= N:  # 부모 노드 i
        make_tree(i * 2)  # 왼쪽 자식 노드

        tree[i] = number  # 부모 노드
        number += 1

        make_tree(i * 2 + 1)  # 오른쪽 자식 노드


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)
    number = 1
    make_tree(1)

    print(f"#{test_case} {tree[1]} {tree[N // 2]}")
