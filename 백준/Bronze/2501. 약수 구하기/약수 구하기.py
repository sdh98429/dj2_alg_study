N, K = map(int, input().split())

C = []

for i in range(1, N+1):
  if not N%i:
    C.append(i)

if K <= len(C):
  print(C[K-1])
else:
  print(0)