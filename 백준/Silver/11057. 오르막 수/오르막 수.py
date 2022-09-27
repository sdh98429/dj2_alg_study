N = int(input())

DP = [[0] * 10 for _ in range(N)]
DP[0] = [1] * 10

for i in range(1, N):
  for j in range(10):
    DP[i][j] = sum(DP[i-1][0:j+1])

print(sum(DP[N-1])%10007)