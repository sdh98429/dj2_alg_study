def ascend(num, ind, L):
  if len(num) == M:
    print(*num)
    return 
  for i in range(ind, len(L)):
    ascend(num+[L[i]], i, L)

N, M = map(int, input().split())
L = list(map(int, input().split()))
L = list(set(L))
L.sort()

ascend([], 0, L)