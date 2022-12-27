import sys
input = sys.stdin.readline
N = int(input())

DP_R = [0] * N
DP_G = [0] * N
DP_B = [0] * N

Cost = [0] * N
for i in range(N):
  Cost[i] = list(map(int, input().split()))

DP_R[0] = Cost[0][0]
DP_G[0] = Cost[0][1]
DP_B[0] = Cost[0][2]

for i in range(1, N):
  DP_R[i] = Cost[i][0] + min(DP_G[i-1], DP_B[i-1])
  DP_G[i] = Cost[i][1] + min(DP_R[i-1], DP_B[i-1])
  DP_B[i] = Cost[i][2] + min(DP_R[i-1], DP_G[i-1])
print(min(DP_R[N-1], DP_G[N-1], DP_B[N-1]))