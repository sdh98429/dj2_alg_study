# 2xn 타일링

N = int(input())

DP = [1, 2] + [0] * 1000

for i in range(2, 1000):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[N-1]%10007)