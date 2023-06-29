L = list(map(int, input().split()))
L.sort()
if L[1] - L[0] == L[2] - L[1]:
  print(2 * L[2] - L[1])
else:
  print(L[0] + L[2] - L[1])
  