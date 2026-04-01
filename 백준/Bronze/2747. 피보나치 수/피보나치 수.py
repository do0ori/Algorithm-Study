N = int(input())
fb = [0] * (N + 1)
fb[0] = 0
fb[1] = 1
for i in range(2, N + 1):
    fb[i] = fb[i - 1] + fb[i - 2]

print(fb[N])
