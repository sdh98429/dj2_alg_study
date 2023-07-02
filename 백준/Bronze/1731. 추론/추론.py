N = int(input())
L = []
for _ in range(N):
  L.append(int(input()))

if L[2] - L[1] == L[1] - L[0]:
  print(L[-1] + L[1] - L[0])
else:
  print(L[-1] * (L[1]//L[0]))