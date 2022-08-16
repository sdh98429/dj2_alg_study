N, M = map(int, input().split())

from itertools import combinations

L = list(combinations(list(i for i in range(1, N+1)), M))

for l in L:
  print(*l)