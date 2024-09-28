T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    numbers = sorted(list(map(int, input().split())))

    answer = []
    for i in range(5):
        answer.append(numbers[-i - 1])
        answer.append(numbers[i])

    print(f'#{test_case} {" ".join(map(str, answer))}')
