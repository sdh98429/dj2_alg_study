from itertools import permutations

N = int(input())
Perm = permutations([i for i in range(1, N+1)], N)
for perm in Perm:
  print(*perm)