N = int(input())
A = list(map(int, input().split()))

DP = [1] * N
DP_R = [1] * N

for i in range(N):
  for j in range(i):
    if A[i] > A[j]:
      DP[i] = max(DP[i], DP[j]+1)

for i in range(N-1, -1, -1):
  for j in range(N-1, i, -1):
    if A[i] > A[j]:
      DP_R[i] = max(DP_R[i], DP_R[j]+1)

DP_B = [x+y-1 for x, y in zip(DP, DP_R)]
print(max(DP_B))