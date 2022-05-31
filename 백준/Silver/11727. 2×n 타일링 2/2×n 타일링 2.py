N = int(input())

DP = [1, 3] + [0] * (N-2)

for i in range(2, N):
    DP[i] = DP[i-1] + DP[i-2] * 2
print(DP[N-1]%10007)