M, N = map(int, input().split())

P = [0, 0] + [1] * 1000000
for i in range(len(P)):
  if P[i]:
    for j in range(2, (len(P)//i)):
      P[i*j] = 0

for i in range(M, N+1):
  if P[i]:
    print(i)