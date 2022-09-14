T = int(input())

DP = [1] * 100

for i in range(3, 100):
  DP[i] = DP[i-2] + DP[i-3]

for tc in range(T):
  N = int(input())
  print(DP[N-1])