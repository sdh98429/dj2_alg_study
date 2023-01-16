
P = [False, False] + [True] * 123456 * 2

for i in range(int(len(P)**0.5)+1):
  if P[i]:
    j = 2
    while i*j in range(len(P)):
      P[i*j] = False
      j += 1


while True:
  N = int(input())
  if not N:
    break
  tot = 0
  for k in range(N+1, 2*N+1):
    try:
      if P[k]:
        tot += 1
    except:
      break
  print(tot)