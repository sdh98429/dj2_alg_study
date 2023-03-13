T = int(input())

for tc in range(T):
  L = list(map(int, input().split()))
  L.sort(reverse=True)
  print(L[2])