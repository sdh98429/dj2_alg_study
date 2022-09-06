N = int(input())
Plan = [0] * 30
for i in range(N):
  Plan[i] = tuple(map(int, input().split()))

DP = [0] * 30
for i in range(N):
  if DP[i+1] < DP[i]:
    DP[i+1] = DP[i]
  if DP[i+Plan[i][0]] < DP[i] + Plan[i][1]:
    DP[i+Plan[i][0]] = DP[i] + Plan[i][1]

print(DP[N])