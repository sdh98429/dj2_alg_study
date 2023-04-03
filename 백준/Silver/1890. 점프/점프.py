N = int(input())
L = list()
for _ in range(N):
  L.append(list(map(int, input().split())))

DP = [[0]*N for _ in range(N)]
DP[0][0] = 1

for i in range(N):
  for j in range(N):
    if i == N-1 and j == N-1:
      break
    d = L[i][j]
    if i+d in range(N):
      DP[i+d][j] += DP[i][j]
    if j+d in range(N):
      DP[i][j+d] += DP[i][j]


print(DP[N-1][N-1])