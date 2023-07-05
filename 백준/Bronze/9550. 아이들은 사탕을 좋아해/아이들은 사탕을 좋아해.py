T = int(input())

for tc in range(1, T+1):
  N, K = map(int, input().split())
  L = list(map(int, input().split()))
  tot = 0
  for l in L:
    tot += l//K
  print(tot)
  