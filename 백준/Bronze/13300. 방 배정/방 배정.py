N, K = map(int, input().split())

L = [[0, 0] for _ in range(6)]
for _ in range(N):
  S, Y = map(int, input().split())
  L[Y-1][S] += 1

tot = 0
for l in L:
  tot += l[0]//K + (1 if l[0]%K else 0)
  tot += l[1]//K + (1 if l[1]%K else 0)
print(tot)