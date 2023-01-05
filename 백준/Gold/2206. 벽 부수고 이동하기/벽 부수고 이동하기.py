from collections import deque

def BFS():
  global visited_ori, visited_break
  q = deque()
  q.append((0, 0, 1, True))
  visited_ori[0][0] = 1
  while q:
    vi, vj, tot, bomb = q.popleft()
      
    if vi == N-1 and vj == M-1:
      print(tot)
      return
    
    for ddr in dr:
      wi, wj = vi + ddr[0], vj + ddr[1]
      if wi in range(N) and wj in range(M):
        if not bomb:
          if maze[wi][wj] == '0' and not visited_break[wi][wj]:
            visited_break[wi][wj] = 1
            q.append((wi, wj, tot + 1, bomb))
        else:
          if maze[wi][wj] == '0' and not visited_ori[wi][wj]:
            visited_ori[wi][wj] = 1
            q.append((wi, wj, tot + 1, bomb))
          elif maze[wi][wj] == '1' and not visited_break[wi][wj]:
            visited_break[wi][wj] = 1
            q.append((wi, wj, tot + 1, False))
            
            
              
  else:
    print(-1)
    return


dr = [[1, 0], [-1, 0], [0, 1], [0, -1]]


N, M = map(int, input().split())

maze = []
visited_ori = [[0] * M for _ in range(N)]
visited_break = [[0] * M for _ in range(N)]

for _ in range(N):
  maze += [list(input())]

BFS()
