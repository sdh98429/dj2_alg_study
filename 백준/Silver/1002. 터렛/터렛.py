T = int(input())

for tc in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  D_sq = (x1-x2)**2 + (y1-y2)**2
  if D_sq == 0 and r1 == r2:
    print(-1)
  elif D_sq == (r1+r2)**2 or D_sq == (r1-r2)**2:
    print(1)
  elif (r1-r2) ** 2 < D_sq < (r1+r2)**2:
    print(2)
  else:
    print(0)