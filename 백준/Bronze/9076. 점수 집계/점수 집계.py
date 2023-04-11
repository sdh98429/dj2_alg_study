T = int(input())

for tc in range(T):
  L = list(map(int, input().split()))
  L.sort()
  if L[3] - L[1] >= 4:
    print('KIN')
  else:
    print(sum(L[1:4]))