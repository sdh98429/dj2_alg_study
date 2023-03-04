def IncrePer(S):
  if len(S) == M:
    print(*S)
    return
  for l in L:
   IncrePer(S + [l])
      


N, M = map(int, input().split())

L = list(map(int, input().split()))
L.sort()

IncrePer([])