def find_palindrome(N, M, field):
    for r in range(N):
        for c in range(N):
            if c + M <= N:
                pattern = "".join([field[r][c + i] for i in range(M)])
                if pattern == pattern[::-1]:
                    return pattern

            if c - M >= 0:
                pattern = "".join([field[r][c - i] for i in range(M)])
                if pattern == pattern[::-1]:
                    return pattern

            if r + M <= N:
                pattern = "".join([field[r + i][c] for i in range(M)])
                if pattern == pattern[::-1]:
                    return pattern

            if r - M >= 0:
                pattern = "".join([field[r - i][c] for i in range(M)])
                if pattern == pattern[::-1]:
                    return pattern


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    field = [list(input()) for n in range(N)]
    print(f"#{test_case} {find_palindrome(N, M, field)}")
