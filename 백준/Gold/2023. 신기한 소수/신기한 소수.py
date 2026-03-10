import sys

sys.setrecursionlimit(10**8)

input = sys.stdin.readline
N = int(input())


def is_prime(n):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def dfs(n):
    if len(str(n)) == N:
        print(n)
        return

    for i in range(1, 10, 2):
        new_base = n * 10 + i
        if is_prime(new_base):
            dfs(new_base)


for prime_number in [2, 3, 5, 7]:
    dfs(prime_number)
