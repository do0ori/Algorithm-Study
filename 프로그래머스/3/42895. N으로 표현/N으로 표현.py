def solution(N, number):
    # 최솟값이 8이므로 8까지 사용
    dp = [set() for _ in range(8)]
    
    # 각 단계에서 N을 여러 번 사용한 값을 추가 (예: 5, 55, 555, ...)
    for i in range(8):
        dp[i].add(int(str(N) * (i + 1)))

    # 각 단계에서 이전 단계들의 조합으로 만들 수 있는 경우의 수를 추가
    # (괄호는 동적 계획법에서 이전 단계에서 만들어진 값을 가져와서 연산할 때 암묵적으로 사용됨)
    for i in range(8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i - j - 1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        # 만약 number를 만들 수 있다면 해당 단계(i+1) 반환
        if number in dp[i]:
            return i + 1

    # 8번까지 사용해도 못 만들면 -1 반환
    return -1