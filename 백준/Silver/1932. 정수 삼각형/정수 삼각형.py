import sys
input = sys.stdin.readline

N = int(input())

DP_up = [0] * N
DP_down = [0] * N
for i in range(N):
  L = list(map(int, input().split()))
  DP_down[0] = DP_up[0] + L[0]
  for j in range(1, len(L)):
    DP_down[j] = max(DP_up[j-1], DP_up[j]) + L[j]
  DP_up[:] = DP_down[:]
print(max(DP_down))
