def fill_child_sum(i):
    if i > N:  # 유효하지 않은 노드 번호
        return 0

    if tree[i] == 0:  # 채워지지 않은 노드
        left_child = fill_child_sum(2 * i)
        right_child = fill_child_sum(2 * i + 1)
        tree[i] = left_child + right_child

    return tree[i]


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    leaf_nodes = [list(map(int, input().split())) for _ in range(M)]

    tree = [0] * (N + 1)
    for node, value in leaf_nodes:
        tree[node] = value

    fill_child_sum(1)

    print(f"#{test_case} {tree[L]}")
