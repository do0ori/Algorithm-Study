T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    pairs = list(map(int, input().split()))
    tree = dict()
    for i in range(E):
        parent, child = pairs[2 * i], pairs[2 * i + 1]
        tree[parent] = [*tree.get(parent, []), child]

    node_count = 0
    stack = [N]
    while stack:
        node = stack.pop()

        if node in tree:
            stack.extend(tree[node])

        node_count += 1

    print(f"#{test_case} {node_count}")
