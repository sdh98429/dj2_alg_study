M = int(input())
N = int(input())

L = [0, 0] + [1] * (N-1)
for p in range(2, int(N**0.5)+1):
  if L[p]:
    q = 2
    while True:
      try:
        L[p*q] = 0
        q += 1
      except:
        break
min_p = 0
tot = 0
for i in range(M, N+1):
  if L[i]:
    tot += i
    if not min_p:
      min_p = i

if min_p:
  print(tot)
  print(min_p)
else:
  print(-1)