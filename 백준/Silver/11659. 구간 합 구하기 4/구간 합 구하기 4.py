import sys
M, N = map(int, sys.stdin.readline().split())
L = list(map(int ,sys.stdin.readline().split()))
L_sum = [0] * M
L_sum[0] = L[0]
for i in range(1, M):
  L_sum[i] = L_sum[i-1] + L[i]
for _ in range(N):
  i, j = map(int, sys.stdin.readline().split())
  print(L_sum[j-1] - (L_sum[i-2] if i > 1 else 0))