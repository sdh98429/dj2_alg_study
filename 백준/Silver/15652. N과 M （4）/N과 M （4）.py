def Recursion(ind, L):
  if ind == 0:
    print(*L)
    return
  for i in range(L[-1], N+1):
    Recursion(ind-1, L + [i])

N, M = map(int, input().split())

for i in range(1, N+1):
  Recursion(M-1, [i])