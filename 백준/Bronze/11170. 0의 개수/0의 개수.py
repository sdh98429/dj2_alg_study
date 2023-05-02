T = int(input())
for tc in range(T):
  N, M = map(int, input().split())
  tot = 0
  for i in range(N, M+1):
    for s in str(i):
      if s == '0':
        tot += 1
  print(tot)