N, K = map(int, input().split())

cargo = [[0, 0]] * (N+1)
for i in range(1,N+1):
  cargo[i] = list(map(int, input().split()))

DP = [[0] * (K+1)] * (N+1)
DP = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
  for j in range(1,K+1):
    w = cargo[i][0]
    v = cargo[i][1]

    flag = False
    if j < w:
      DP[i][j] = DP[i-1][j]
    else:
      flag = True
      DP[i][j]=max( DP[i-1][j],DP[i-1][j-w]+v)

print(DP[N][K])
