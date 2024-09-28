T = int(input())
for test_case in range(1, T + 1):
    num_color = int(input())
    area = [[set() for _ in range(10)] for _ in range(10)]
    for _ in range(num_color):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                area[r][c].add(color)
    purple = 0
    for r in range(10):
        for c in range(10):
            if area[r][c] == {1, 2}:
                purple += 1
    print(f"#{test_case} {purple}")
