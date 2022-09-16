from itertools import permutations
N, M = map(int, input().split())
L = list(map(int, input().split()))
P = list(permutations(L, M))
P.sort()
for p in P:
  print(*p)