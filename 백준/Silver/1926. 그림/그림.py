import sys
input = sys.stdin.readline

from collections import deque

dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def BFS(i, j):
  global visited, pic_max
  Q = deque()
  Q.append([i,j])
  pic_area = 0
  visited[i][j] = 1
  while Q:
    vi, vj = Q.popleft()
    pic_area += 1
    for r in range(4):
      wi, wj = vi + dr[r][0], vj + dr[r][1]
      if wi in range(N) and wj in range(M) and not visited[wi][wj] and L[wi][wj]:
        Q.append([wi, wj])
        visited[wi][wj] = 1
  else:
    if pic_area > pic_max:
      pic_max = pic_area

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
pic_cnt = 0
pic_max = 0
for i in range(N):
  for j in range(M):
    if not visited[i][j] and L[i][j]:
      pic_cnt += 1
      BFS(i,j)
print(pic_cnt)
print(pic_max)

