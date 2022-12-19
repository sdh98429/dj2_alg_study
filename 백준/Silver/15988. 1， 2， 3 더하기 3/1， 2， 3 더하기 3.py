import sys
input = sys.stdin.readline

T = int(input())

DP = [1, 2, 4] + [0] * 1000000

for i in range(3, 1000000):
  DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) %1000000009


for tc in range(T):
  N = int(input())
  print(DP[N-1])

