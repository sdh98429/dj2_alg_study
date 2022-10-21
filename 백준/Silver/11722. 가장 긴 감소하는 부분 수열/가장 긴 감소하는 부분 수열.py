N = int(input())
A = list(map(int, input().split()))
DP = [1] * N

for i in range(1, N):
  for j in range(i):
    if A[j] > A[i]:
      if DP[j] + 1 > DP[i]:
        DP[i] = DP[j] + 1
print(max(DP))