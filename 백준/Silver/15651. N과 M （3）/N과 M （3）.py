def Recursive(ind, l):
  global N, M
  if ind == M:
    print(*l)
    return
  for i in range(1, N+1):
    Recursive(ind+1, l + [i])

N, M = map(int, input().split())
Recursive(0, [])