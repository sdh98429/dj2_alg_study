N, M = map(int, input().split())
B = [0] * N
for _ in range(M):
  i, j, k = map(int, input().split())
  for ind in range(i, j+1):
    B[ind-1] = k
print(*B)