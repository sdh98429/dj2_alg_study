def Cut(paper):
  global plus_cnt, zero_cnt, minus_cnt
  size = len(paper)

  before = paper[0][0]
  flag = True
  if size != 1:
    for i in range(size):
      for j in range(size):
        if flag and before != paper[i][j]:
          flag = False
          break
  if flag or size == 1:
    if paper[0][0] == 1:
      plus_cnt += 1
    elif paper[0][0] == 0:
      zero_cnt += 1
    elif paper[0][0] == -1:
      minus_cnt += 1
    return
  else:
    for i in range(3):
      for j in range(3):
        Cut([row[(size//3)*i:(size//3)*(i+1)] for row in paper[(size//3)*j:(size//3)*(j+1)]])

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]
minus_cnt = 0
zero_cnt = 0
plus_cnt = 0

Cut(L)
print(minus_cnt)
print(zero_cnt)
print(plus_cnt)
