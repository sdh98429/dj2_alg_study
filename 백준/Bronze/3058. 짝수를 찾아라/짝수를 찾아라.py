T = int(input())
for tc in range(T):
  tot = 0
  even_min = 9876543210
  L = list(map(int, input().split()))
  for l in L:
    if not l%2:
      tot += l
      if l < even_min:
        even_min = l
  print(tot, even_min)