def GCD(a, b):
  while a:
    a, b = b%a, a
  return b

T = int(input())
for tc in range(T):
  L = list(map(int, input().split()))
  tot = 0
  for i in range(1, L[0]):
    for j in range(i+1, L[0]+1):
      tot += GCD(L[i], L[j])
  print(tot)