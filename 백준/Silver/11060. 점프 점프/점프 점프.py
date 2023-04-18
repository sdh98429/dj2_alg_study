import sys
input = sys.stdin.readline

N = int(input())
# L = [[0, 987654321]*N]
L = list(map(int, input().split()))
DP = [0] + [987654321] * (N-1)

for i in range(N):
  for j in range(1, L[i]+1):
    if i + j in range(N):
      DP[i+j] = min(DP[i]+1, DP[i+j])
print(DP[-1] if DP[-1] != 987654321 else -1)