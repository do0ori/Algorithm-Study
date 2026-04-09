def dfs(start, path):
    if len(path) == 6:
        print(*path)
        return

    for i in range(start, len(S)):
        path.append(S[i])
        dfs(i + 1, path)
        path.pop()


while True:
    K, *S = map(int, input().split())
    if K == 0:
        break

    dfs(0, [])
    print()
