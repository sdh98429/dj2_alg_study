L = []
for i in range(1, 50):
  for j in range(i):
    L.append(i)
A, B = map(int, input().split())
ans = 0
for i in range(A-1, B):
  ans += L[i]
print(ans)