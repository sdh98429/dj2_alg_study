L = [list(map(int, input().split())) for _ in range(9)]

max_num = -1
max_i, max_j = -1, -1

for i in range(9):
  for j in range(9):
    if L[i][j] > max_num:
      max_num = L[i][j]
      max_i, max_j = i, j
print(max_num)
print(max_i+1, max_j+1)