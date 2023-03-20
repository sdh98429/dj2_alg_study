def PermAscend(ind, P):
  if len(P) == M:
    print(*P)
    return P
  if ind == N:
    return
  for i in range(ind, N):
    PermAscend(i+1, P+[L[i]])

N, M = map(int, input().split())
L = list(map(int, input().split()))
L.sort()
PermAscend(0, [])