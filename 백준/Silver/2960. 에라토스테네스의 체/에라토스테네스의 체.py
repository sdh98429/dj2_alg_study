N, K = map(int, input().split())

P = [False, False, True] + [True] * (N-2)

k = 0

for i in range(2, N+1):
  if P[i]:
    j = 1
    while i*j in range(len(P)):
      if P[i*j]:
        k += 1
        if k == K:
          print(i*j)
          break
      P[i*j] = False
      j += 1
