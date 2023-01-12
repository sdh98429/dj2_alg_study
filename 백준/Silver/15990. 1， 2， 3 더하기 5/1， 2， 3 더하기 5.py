import sys
input = sys.stdin.readline

T = int(input())
DP = [[0, 0, 0] for _ in range(100000)]
DP[0] = [1, 0, 0]
DP[1] = [0, 1, 0]
DP[2] = [1, 1, 1]

for i in range(3, 100000):
  DP[i][0] = (DP[i-1][1] + DP[i-1][2])%1000000009
  DP[i][1] = (DP[i-2][0] + DP[i-2][2])%1000000009
  DP[i][2] = (DP[i-3][0] + DP[i-3][1])%1000000009



for tc in range(T):
  N = int(input())
  print(sum(DP[N-1])%1000000009)