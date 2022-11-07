import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

def bfs(v):
  q = deque()
  q.append(v)
  visited_bfs[v] = 1
  while q:
    v = q.popleft()
    print(v, end=" ")
    for i in range(1, N+1):
      if graph[v][i] and not visited_bfs[i]:
        q.append(i)
        visited_bfs[i] = 1

def dfs(v):
  visited_dfs[v] = 1
  print(v, end=" ")
  for i in range(1, N+1):
    if graph[v][i] and not visited_dfs[i]:
      dfs(i)
graph = [[0] * (N+1) for _ in range(N+1)]
visited_bfs = [0] * (N+1)
visited_dfs = [0] * (N+1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a][b] = graph[b][a] = 1

dfs(V)
print()
bfs(V)
