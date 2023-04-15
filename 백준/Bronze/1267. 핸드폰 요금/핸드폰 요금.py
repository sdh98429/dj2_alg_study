N = int(input())
L = list(map(int, input().split()))
tot_Y = 0
tot_M = 0
for l in L:
  tot_Y += (l//30+1) * 10 
  tot_M += (l//60+1) * 15 
if tot_Y == tot_M:
  print('Y', 'M', tot_Y)
else:
  if tot_Y < tot_M:
    print('Y', tot_Y)
  else:
    print('M', tot_M)