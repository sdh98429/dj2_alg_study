N = int(input())
L = list(map(int, input().split()))

DP = [i for i in L]

for i in range(1, N):
  for j in range(i):
    if L[j] < L[i]:
      if DP[i] < DP[j] + L[i]:
        DP[i] = DP[j] + L[i]
print(max(DP))