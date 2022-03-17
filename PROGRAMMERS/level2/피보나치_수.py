# ! 피보나치 수, dp
# 12945

def solution(n):
    dp = [0, 1] + [0] * (n-1)
    for i in range(n-1):
        dp[i+2] = dp[i+1] + dp[i]
    return dp[n]%1234567

# n	return
# 3	2
# 5	5