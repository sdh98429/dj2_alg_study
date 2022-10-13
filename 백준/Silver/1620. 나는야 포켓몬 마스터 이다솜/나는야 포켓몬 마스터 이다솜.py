N, M = map(int, input().split())
D = dict()
for i in range(1, N+1):
  P = input()
  D[i] = P
  D[P] = i

for _ in range(M):
  K = input()
  try:
    print(D[int(K)])
  except:
    print(D[K])