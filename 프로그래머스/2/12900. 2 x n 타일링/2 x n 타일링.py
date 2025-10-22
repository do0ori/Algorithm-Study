"""
f(1) = 1
f(2) = 2
f(3) = f(1) + f(2) = 3
"""
def solution(n):
    dp = [0, 1, 2]
    if n < 3:
        return dp[n]
    
    prev1 = dp[1]
    prev2 = dp[2]
    for i in range(3, n+1):
        temp = prev1
        prev1 = prev2
        prev2 = temp + prev2
        
    return prev2 % 1000000007