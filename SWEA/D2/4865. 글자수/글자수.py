T = int(input())
for test_case in range(1, T + 1):
    str1 = set(input())
    str2 = input()
    char_count = {s: str2.count(s) for s in str1}
    print(f"#{test_case} {max(char_count.values())}")
