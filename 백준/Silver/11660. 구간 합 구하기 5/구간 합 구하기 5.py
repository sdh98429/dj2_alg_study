import sys
input = sys.stdin.readline
N, M = map(int, input().split())

L = [[0] * (N+1)]
L_sum = [[0] * (N+1) for _ in range(N+1)]
for _ in range(N):
  L.append([0] + list(map(int, input().split())))
for i in range(1, N+1):
  for j in range(1, N+1):
    L_sum[i][j] = L_sum[i][j-1] + L_sum[i-1][j]+L[i][j] -L_sum[i-1][j-1]

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  print(L_sum[x2][y2]-L_sum[x2][y1-1]-L_sum[x1-1][y2]+L_sum[x1-1][y1-1])