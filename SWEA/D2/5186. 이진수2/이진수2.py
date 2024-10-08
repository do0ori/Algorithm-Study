def convert_decimal(num, base):
    result = []
    d = num
    while d != 0:
        mult = d * base
        i, d = int(mult), mult - int(mult)
        result.append(i)

    return "".join(map(str, result)) if len(result) <= 12 else "overflow"


T = int(input())
for test_case in range(1, T + 1):
    N = float(input())
    binary_decimal = convert_decimal(N, 2)

    print(f"#{test_case} {binary_decimal}")
