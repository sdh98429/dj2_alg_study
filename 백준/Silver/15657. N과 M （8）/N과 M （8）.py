def NonDescend(P, ind):
  if len(P) == M:
    print(*P)
    return
  for i in range(ind, len(L)):
    NonDescend(P+[L[i]], i)


N, M = map(int, input().split())
L = sorted(list(map(int, input().split())))
NonDescend([], 0)
