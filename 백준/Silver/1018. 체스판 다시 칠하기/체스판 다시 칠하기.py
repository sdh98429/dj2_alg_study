Part = [[['B']*8 for _ in range(8)] for _ in range(2)]

for i in range(8):
  for j in range(8):
    if (i+j)%2:
      Part[0][i][j]='W'
    else:
      Part[1][i][j]='W'
    

N, M = map(int, input().split())
L = [list(input()) for _ in range(N)]

min_tot = 987654321
for x in range(N-7):
  for y in range(M-7):
    tot_1 = 0
    tot_2 = 0
    for i in range(8):
      for j in range(8):
        if Part[0][i][j] != L[x+i][y+j]:
          tot_1 += 1
        if Part[1][i][j] != L[x+i][y+j]:
          tot_2 += 1
    min_tot = min(min_tot, tot_1, tot_2)
print(min_tot)