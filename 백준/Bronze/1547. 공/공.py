M = int(input())
C = [1, 0, 0]
for _ in range(M):
  X, Y = map(int, input().split())
  X, Y = X-1, Y-1
  C[X], C[Y] = C[Y], C[X]

for i in range(3):
  if C[i]:
    print(i+1)