def convert(num, base):
    result = []
    q = num
    while q > 0:
        q, r = divmod(q, base)
        result.append(r)

    return "".join(map(str, result[::-1])).zfill(4 * N)


T = int(input())
for test_case in range(1, T + 1):
    N, oct_num = input().split()
    N = int(N)
    binary_num = convert(int(oct_num, 16), 2)

    print(f"#{test_case} {binary_num}")
