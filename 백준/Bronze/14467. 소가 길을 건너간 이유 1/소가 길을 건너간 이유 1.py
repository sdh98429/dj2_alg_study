N = int(input())
L = ['start'] * 10
move_cnt = 0
for _ in range(N):
  cow, loc = map(int, input().split())
  if L[cow-1] == 'start':
    L[cow-1] = loc
  else:
    if L[cow-1] != loc:
      move_cnt += 1
      L[cow-1] = loc

print(move_cnt)