def solution(arr):
    # 숫자와 연산자를 분리
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = [arr[i] for i in range(1, len(arr), 2)]
    n = len(nums)

    # dp 테이블 초기화
    #   dp_max[i][j]: i번째 숫자부터 j번째 숫자까지의 수식에서 만들 수 있는 최댓값.
    #   dp_min[i][j]: i번째 숫자부터 j번째 숫자까지의 수식에서 만들 수 있는 최솟값.
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]
    
    # 숫자 하나만으로 이루어진 수식은 해당 숫자로 초기화
    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]

    # 부분 수식의 길이를 2, 3, ... n까지 늘려가며 DP 테이블 갱신
    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            dp_max[i][j] = float('-inf')
            dp_min[i][j] = float('inf')
            
            # 중간에 있는 연산자 기준으로 좌우 부분 나눠서 계산
            for k in range(i, j):
                if ops[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                elif ops[k] == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])

    # 전체 수식의 최댓값 반환
    return dp_max[0][n - 1]
