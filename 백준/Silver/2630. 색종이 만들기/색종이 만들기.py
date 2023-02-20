
white_cnt = 0
blue_cnt = 0

def Cut(paper):
  global white_cnt, blue_cnt
  size = len(paper)
  if size == 1:
    if paper[0][0] == 1:
      blue_cnt += 1
    else:
      white_cnt += 1
    return

  before = paper[0][0]
  flag = True
  for i in range(size):
    for j in range(size):
      if flag and paper[i][j] != before:
        Cut([row[:size//2] for row in paper[:size//2]])
        Cut([row[:size//2] for row in paper[size//2:]])
        Cut([row[size//2:] for row in paper[:size//2]])
        Cut([row[size//2:] for row in paper[size//2:]])
        flag = False
        break
  if flag:
    if paper[0][0] == 1:
      blue_cnt += 1
    else:
      white_cnt += 1


N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

Cut(L)
print(white_cnt)
print(blue_cnt)